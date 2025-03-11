import abc
import hashlib
import logging
import sqlite3
import sys
import urllib.parse
from pyhindsight import utils

log = logging.getLogger(__name__)


class WebBrowser(object):
    def __init__(
            self, profile_path, browser_name, cache_path=None, version=None, display_version=None,
            timezone=None, structure=None, no_copy=None, temp_dir=None):
        self.profile_path = profile_path
        self.browser_name = browser_name
        self.cache_path = cache_path
        self.version = version
        self.display_version = display_version
        self.timezone = timezone
        self.structure = structure
        self.parsed_artifacts = []
        self.parsed_storage = []
        self.parsed_extension_data = []
        self.artifacts_counts = {}
        self.artifacts_display = {}
        self.preferences = []
        self.no_copy = no_copy
        self.temp_dir = temp_dir
        self.origin_hashes = {}
        self.installed_extensions = {}

        if self.version is None:
            self.version = []

    @staticmethod
    def format_processing_output(name, items):
        width = 80
        left_side = width*0.55
        count = '{:>6}'.format(str(items))
        pretty_name = "{name:>{left_width}}:{count:^{right_width}}" \
            .format(name=name, left_width=int(left_side), count=' '.join(['[', count, ']']),
                    right_width=(width - int(left_side)-2))
        return pretty_name

    @staticmethod
    def format_profile_path(profile_path):
        if len(profile_path) > 68:
            profile_path = "...{}".format(profile_path[-65:])
        return "\n    Profile: {}".format(profile_path)

    def build_structure(self, path, database):

        if database not in list(self.structure.keys()):
            self.structure[database] = {}

            # Copy and connect to copy of SQLite DB
            conn = utils.open_sqlite_db(self, path, database)
            if not conn:
                self.artifacts_counts[database] = 'Failed'
                return
            cursor = conn.cursor()

            # Find the names of each table in the db
            try:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = cursor.fetchall()
            except sqlite3.OperationalError:
                print("\nSQLite3 error; is the Chrome profile in use?  Hindsight cannot access history files "
                      "if Chrome has them locked.  This error most often occurs when trying to analyze a local "
                      "Chrome installation while it is running.  Please close Chrome and try again.")
                sys.exit(1)
            except:
                log.error(f' - Could not query {database} in {path}')
                return

            # For each table, find all the columns in it
            for table in tables:
                # cursor.execute('PRAGMA table_info({})'.format(str(table[0])))
                cursor.execute('PRAGMA table_info({})'.format(table['name']))
                columns = cursor.fetchall()

                # Create a dict of lists of the table/column names
                # self.structure[database][str(table[0])] = []
                self.structure[database][table['name']] = []
                for column in columns:
                    self.structure[database][table['name']].append(column['name'])

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_clean_hostnames(self):
        hostnames = set()
        for artifact in self.parsed_artifacts:
            if not isinstance(artifact, self.HistoryItem) or not artifact.url:
                continue

            # Some artifact "URLs", often parsed from Preferences, are two
            # origins combined, so split them into two.
            # Example from Preferences (3pcd_heuristics_grants):
            #   "https://[*.]lnkd.in,https://[*.]linkedin.com"
            artifact_urls = artifact.url.split(',')

            for artifact_url in artifact_urls:
                # Some artifact "URLs" will be in invalid forms, which urllib (rightly)
                # won't parse. Modify these URLs so they will parse properly.
                # Examples:
                #   Cookie: ".example.com",
                #   Preferences (cookie_controls_metadata): "https://[*.]example.com"
                prefixes = ('.', 'https://[*.]', 'http://[*.]')

                for prefix in prefixes:
                    if artifact_url.startswith(prefix):
                        artifact_url = 'https://' + artifact_url[len(prefix):]

                if artifact_url.endswith(',*'):
                    artifact_url = artifact_url[:-2]

                try:
                    hostname = urllib.parse.urlparse(artifact_url).hostname
                except ValueError as e:
                    log.warning(f'Error when parsing domain from {artifact_url}; {e}')
                    continue

                # Some URLs don't have a domain, like local PDF files
                if hostname:
                    hostnames.add(hostname)
        return hostnames

    def build_md5_hash_list_of_origins(self):
        domains = self.get_clean_hostnames()
        for domain in domains:
            self.origin_hashes[hashlib.md5(domain.encode()).hexdigest()] = domain

    def get_extension_name_from_id(self, extension_id):
        if self.installed_extensions and self.installed_extensions.get('data'):
            for extension in self.installed_extensions['data']:
                if extension.ext_id == extension_id:
                    return extension.name
            return "<Extension not found - may have been uninstalled>"
        return "<Unable to parse installed extensions>"

    class HistoryItem(object):
        def __init__(self, item_type, timestamp, profile, url=None, name=None, value=None, interpretation=None):
            self.row_type = item_type
            self.timestamp = timestamp
            self.profile = profile
            self.url = url
            self.name = name
            self.value = value
            self.interpretation = interpretation

        def __lt__(self, other):
            if not self.timestamp.tzinfo and other.timestamp.tzinfo:
                log.warning(f'{self} missing tzinfo; using tzinfo from {other} during sort')
                self.timestamp = self.timestamp.replace(tzinfo=other.timestamp.tzinfo)
            elif self.timestamp.tzinfo and not other.timestamp.tzinfo:
                log.warning(f'{other} missing tzinfo; using tzinfo from {self} during sort')
                other.timestamp = other.timestamp.replace(tzinfo=self.timestamp.tzinfo)

            return self.timestamp < other.timestamp

        def __iter__(self):
            return iter(self.__dict__)

    class URLItem(HistoryItem):
        def __init__(
                self, profile, visit_id, url, title, visit_time, last_visit_time, visit_count, typed_count, from_visit,
                transition, hidden, favicon_id, indexed=None, visit_duration=None, visit_source=None,
                transition_friendly=None):
            super(WebBrowser.URLItem, self).__init__('url', timestamp=visit_time, profile=profile, url=url, name=title)
            self.profile = profile
            self.url = url
            self.title = title
            self.visit_time = visit_time
            self.last_visit_time = last_visit_time
            self.visit_count = visit_count
            self.typed_count = typed_count
            self.transition = transition
            self.hidden = hidden
            self.favicon_id = favicon_id
            self.indexed = indexed
            self.visit_id = visit_id
            self.from_visit = from_visit
            self.visit_duration = visit_duration
            self.visit_source = visit_source
            self.transition_friendly = transition_friendly

    class CacheItem(HistoryItem):
        def __init__(
                self, profile, url, title, request_time, locations, key, metadata, data):
            super(WebBrowser.CacheItem, self).__init__('cache', timestamp=request_time, profile=profile, url=url, name=title)
            self.profile = profile
            self.url = url
            self.title = title
            self.locations = locations
            self.key = key
            self.metadata = metadata
            self.data = data
            self.data_summary = None
            self.http_headers_str = None
            self.etag = None
            self.last_modified = None
            self.locations_str = None

        def create_data_summary(self):
            if not self.data:
                return "<no data>"

            if not self.metadata:
                return f"{len(self.data)} bytes"

            return f"{(self.metadata.get_attribute('content-type') or ['not specified'])[0]} ({len(self.data)} bytes)"

        def stringify_http_headers(self):
            headers = {}
            for attribute, value in self.metadata.http_header_attributes:
                headers[attribute] = value

            self.http_headers_str = str(headers)

    class DownloadItem(HistoryItem):
        def __init__(
                self, profile, download_id, url, received_bytes, total_bytes, state, full_path=None, start_time=None,
                end_time=None, target_path=None, current_path=None, opened=None, danger_type=None,
                interrupt_reason=None, etag=None, last_modified=None, chain_index=None, interrupt_reason_friendly=None,
                danger_type_friendly=None, state_friendly=None, status_friendly=None):
            super(WebBrowser.DownloadItem, self).__init__('download', timestamp=start_time, profile=profile, url=url)
            self.profile = profile
            self.download_id = download_id
            self.url = url
            self.received_bytes = received_bytes
            self.total_bytes = total_bytes
            self.state = state
            self.full_path = full_path
            self.start_time = start_time
            self.end_time = end_time
            self.target_path = target_path
            self.current_path = current_path
            self.opened = opened
            self.danger_type = danger_type
            self.interrupt_reason = interrupt_reason
            self.etag = etag
            self.last_modified = last_modified
            self.chain_index = chain_index
            self.interrupt_reason_friendly = interrupt_reason_friendly
            self.danger_type_friendly = danger_type_friendly
            self.state_friendly = state_friendly
            self.status_friendly = status_friendly

    class CookieItem(HistoryItem):
        def __init__(self, profile, host_key, path, name, value, creation_utc, last_access_utc, secure, http_only,
                     persistent=None, has_expires=None, expires_utc=None, priority=None):
            super(WebBrowser.CookieItem, self).__init__(
                'cookie', timestamp=creation_utc, profile=profile, url=host_key, name=name, value=value)
            self.profile = profile
            self.host_key = host_key
            self.path = path
            self.name = name
            self.value = value
            self.creation_utc = creation_utc
            self.last_access_utc = last_access_utc
            self.secure = secure
            self.httponly = http_only
            self.persistent = persistent
            self.has_expires = has_expires
            self.expires_utc = expires_utc
            self.priority = priority

    class AutofillItem(HistoryItem):
        def __init__(self, profile, date_created, name, value, count):
            super(WebBrowser.AutofillItem, self).__init__(
                'autofill', timestamp=date_created, profile=profile, name=name, value=value)
            self.profile = profile
            self.date_created = date_created
            self.name = name
            self.value = value
            self.count = count

    class BookmarkItem(HistoryItem):
        def __init__(self, profile, date_added, name, url, parent_folder, sync_transaction_version=None):
            super(WebBrowser.BookmarkItem, self).__init__(
                'bookmark', timestamp=date_added, profile=profile, name=name, value=parent_folder)
            self.profile = profile
            self.date_added = date_added
            self.name = name
            self.url = url
            self.parent_folder = parent_folder
            self.sync_transaction_version = sync_transaction_version

    class BookmarkFolderItem(HistoryItem):
        def __init__(self, profile, date_added, date_modified, name, parent_folder, sync_transaction_version=None):
            super(WebBrowser.BookmarkFolderItem, self).__init__(
                'bookmark folder', timestamp=date_added, profile=profile, name=name, value=parent_folder)
            self.profile = profile
            self.date_added = date_added
            self.date_modified = date_modified
            self.name = name
            self.parent_folder = parent_folder
            self.sync_transaction_version = sync_transaction_version

    class BrowserExtension(object):
        def __init__(self, profile, ext_id, name, description, version, permissions, manifest):
            self.profile = profile
            self.ext_id = ext_id
            self.name = name
            self.description = description
            self.version = version
            self.permissions = permissions
            self.manifest = manifest

    class LoginItem(HistoryItem):
        def __init__(self, profile, date_created, url, name, value, count, interpretation):
            super(WebBrowser.LoginItem, self).__init__(
                'login', timestamp=date_created, profile=profile, url=url, name=name, value=value)
            self.profile = profile
            self.date_created = date_created
            self.url = url
            self.name = name
            self.value = value
            self.count = count
            self.interpretation = interpretation

    class PreferenceItem(HistoryItem):
        def __init__(self, profile, url, timestamp, key, value, interpretation):
            super(WebBrowser.PreferenceItem, self).__init__(
                'preference', timestamp=timestamp, profile=profile, name=key, value=value)
            self.profile = profile
            self.url = url
            self.timestamp = timestamp
            self.key = key
            self.value = value
            self.interpretation = interpretation

    class SiteSetting(HistoryItem):
        def __init__(self, profile, url, timestamp, key, value, interpretation):
            super(WebBrowser.SiteSetting, self).__init__(
                'site setting', timestamp=timestamp, profile=profile, name=key, value=value)
            self.profile = profile
            self.url = url
            self.timestamp = timestamp
            self.key = key
            self.value = value
            self.interpretation = interpretation

    class MediaItem(HistoryItem):
        def __init__(
                self, profile, url, title, last_updated, position=None, media_duration=None,
                source_title=None, watch_time=None, has_video=None, has_audio=None):
            super(WebBrowser.MediaItem, self).__init__(
                'media', timestamp=last_updated, profile=profile, url=url, name=title)
            self.profile = profile
            self.url = url
            self.title = title
            self.last_updated = last_updated
            self.position = position
            self.media_duration = media_duration
            self.source_title = source_title
            self.watch_time = watch_time
            self.has_video = has_video
            self.has_audio = has_audio

    class StorageItem(object):
        def __init__(self, item_type, profile, origin, key, value=None, seq=None, state=None, source_path=None,
                     last_modified=None, interpretation=None, file_exists=None, file_size=None, magic_results=None):
            self.row_type = item_type
            self.profile = profile
            self.origin = origin
            self.key = key
            self.value = value
            self.seq = seq
            self.state = state
            self.source_path = source_path
            self.last_modified = last_modified
            self.interpretation = interpretation
            self.file_exists = file_exists
            self.file_size = file_size
            self.magic_results = magic_results

        def __lt__(self, other):
            return self.origin < other.origin

        def __iter__(self):
            return iter(self.__dict__)

    class ExtensionStorageItem(StorageItem):
        def __init__(self, profile, extension_id, key, value, extension_name=None, seq=None, state=None, source_path=None, offset=None, was_compressed=None):
            super(WebBrowser.ExtensionStorageItem, self).__init__(
                item_type='extension storage', profile=profile, origin=extension_id, key=key, value=value, seq=seq, state=state, source_path=source_path
            )
            self.profile = profile
            self.extension_id = extension_id
            self.extension_name = extension_name
            self.key = key
            self.value = value
            self.seq = seq
            self.state = state
            self.source_path = source_path
            self.offset = offset
            self.was_compressed = was_compressed

    class LocalStorageItem(StorageItem):
        def __init__(self, profile, origin, key, value, seq, state, source_path, last_modified=None):
            """

            :param profile: The path to the browser profile this item is part of.
            :param origin: The web origin this LocalStorage item belongs to.
            :param key: The key of the LocalStorage item.
            :param value: The value of the LocalStorage item. It will be rendered in UTF-16 if possible; if not, it
            will be shown as a string repr of bytes.
            :param seq: The sequence number of the key.
            :param state: The state of the record (live or deleted).
            :param source_path: The path to the source of the record.
            :param last_modified: Approximation of time content under this origin was last modified.
            If the LocalStorage items were stored in SQLite, this timestamp is when that SQLite file was last modified.
            This means copying the file or otherwise altering the LocalStorage SQLite file's metadata will change this
            value.
            If the LocalStorage items were stored in LevelDB, this will be blank.
            """
            super(WebBrowser.LocalStorageItem, self).__init__(
                'local storage', profile=profile, origin=origin, key=key, value=value, seq=seq, state=state,
                source_path=source_path, last_modified=last_modified)
            self.profile = profile
            self.origin = origin
            self.key = key
            self.value = value
            self.seq = seq
            self.state = state
            self.source_path = source_path
            self.last_modified = last_modified

    class SessionStorageItem(StorageItem):
        def __init__(self, profile, origin, key, value, seq, state, source_path):
            """

            :param profile: The path to the browser profile this item is part of.
            :param origin: The web origin this SessionStorage item belongs to.
            :param key: The key of the SessionStorage item.
            :param value: The value of the SessionStorage item (rendered in UTF-16).
            :param seq: The sequence number of the key.
            :param state: The state of the record (live or deleted).
            :param source_path: The path to the source of the record.
            """
            super(WebBrowser.SessionStorageItem, self).__init__(
                'session storage', profile=profile, origin=origin, key=key, value=value, seq=seq, state=state,
                source_path=source_path)
            self.profile = profile
            self.origin = origin
            self.key = key
            self.value = value
            self.seq = seq
            self.state = state
            self.source_path = source_path

    class IndexedDBItem(StorageItem):
        def __init__(self, profile, origin, key, value, seq, state, database, source_path):
            """

            :param profile: The path to the browser profile this item is part of.
            :param origin: The web origin this IndexedDBItem item belongs to.
            :param key: The key of the IndexedDBItem item.
            :param value: The value of the IndexedDBItem item.
            :param seq: The sequence number.
            :param database: The database within the IndexedDB file the record is part of.
            :param source_path: The path to the source of the record.
            """
            super(WebBrowser.IndexedDBItem, self).__init__(
                'indexeddb', profile=profile, origin=origin, key=key, value=value, seq=seq, state=state,
                source_path=source_path)
            self.profile = profile
            self.origin = origin
            self.key = key
            self.value = value
            self.seq = seq
            self.state = state
            self.database = database
            self.source_path = source_path

    class FileSystemItem(StorageItem):
        def __init__(self, profile, origin, key, value, seq, state, source_path, last_modified=None,
                     file_exists=None, file_size=None, magic_results=None):
            super(WebBrowser.FileSystemItem, self).__init__(
                'file system', profile=profile, origin=origin, key=key, value=value, seq=seq, state=state,
                source_path=source_path, last_modified=last_modified, file_exists=file_exists,
                file_size=file_size, magic_results=magic_results)
            self.profile = profile
            self.origin = origin
            self.key = key
            self.value = value
            self.seq = seq
            self.state = state
            self.source_path = source_path
            self.last_modified = last_modified
            self.file_exists = file_exists
            self.file_size = file_size
            self.magic_results = magic_results
