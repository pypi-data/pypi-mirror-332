from urllib.parse import urlparse

from synapse_sdk.i18n import gettext as _
from synapse_sdk.utils.storage.registry import STORAGE_PROVIDERS


def get_storage(connection_param: str | dict):
    storage_scheme = None
    if isinstance(connection_param, dict):
        storage_scheme = connection_param['provider']
    else:
        storage_scheme = urlparse(connection_param).scheme

    assert storage_scheme in STORAGE_PROVIDERS.keys(), _('지원하지 않는 저장소입니다.')
    return STORAGE_PROVIDERS[storage_scheme](connection_param)


def get_pathlib(storage_config, path_root):
    storage_class = get_storage(storage_config)
    return storage_class.get_pathlib(path_root)
