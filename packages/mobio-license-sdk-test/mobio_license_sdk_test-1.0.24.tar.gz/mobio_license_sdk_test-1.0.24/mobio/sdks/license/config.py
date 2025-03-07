import os
import re
from copy import deepcopy
from mobio.libs.caching import LruCache


class StoreCacheType:
    LOCAL = 1
    REDIS = 2


class Cache:
    class RedisType:
        REPLICA = 1
        CLUSTER = 2

    PREFIX_KEY = "license_sdk_"
    REDIS_URI = "{}?health_check_interval=30".format(os.environ.get("ADMIN_REDIS_URI", os.environ.get("REDIS_URI")))
    REDIS_CLUSTER_URI = "{}?health_check_interval=30".format(os.environ.get("ADMIN_REDIS_CLUSTER_URI",
                                                                            os.environ.get("REDIS_CLUSTER_URI")))
    REDIS_TYPE = int(os.environ.get("ADMIN_REDIS_TYPE", os.environ.get("REDIS_TYPE", "1")))


class UrlConfig:
    ADMIN_CONFIG = "{host}/adm/{version}/merchants/{merchant_id}/configs"
    PARTNER_INFO = "{host}/adm/{version}/partners/{partner_id}/info"
    PARTNER_INFO_CIPHER_ENCRYPT = (
        "{host}/adm/{version}/partners/{partner_id}/info/encrypt"
    )
    ADMIN_GET_FILE_LICENSE = "{host}/adm/{version}/download-license"
    LICENSE_DOWNLOAD_FILE = "{host}/license/api/v1.0/license-merchant/download"
    ADMIN_MERCHANT_PARENT = "{host}/adm/{version}/merchants/{merchant_id}/parent"
    ADMIN_GET_LICENSE_ATTRIBUTE = "{host}/adm/{version}/license/attribute"


class PathDir:
    APPLICATION_DATA_DIR = os.environ.get("APPLICATION_DATA_DIR")
    LICENSE_FOLDER_NAME = "License"
    PATH_DIR_LICENSE_FILE = APPLICATION_DATA_DIR + LICENSE_FOLDER_NAME + "/file_license"


class Mobio:
    vm_type = os.environ.get("VM_TYPE")
    YEK_REWOP = os.environ.get("YEK_REWOP", "f38b67fa-22f3-4680-9d01-c36b23bd0cad")
    MOBIO_TOKEN = "Basic {}".format(YEK_REWOP)
    AUTO_RENEW_FILE_LICENSE = os.environ.get("AUTO_RENEW_LICENSE")
    ADMIN_HOST = os.environ.get("ADMIN_HOST")
    LICENSE_KEY_SALT = os.environ.get("LICENSE_KEY_SALT", "LICENSE_MOBIO_v1_")
    VM_K8S = os.environ.get("K8S")
    # LICENSE_PASS = os.environ.get("LICENSE_PASS", "1")


if Cache.REDIS_TYPE == Cache.RedisType.CLUSTER:
    lru_redis_cache = LruCache(
        store_type=StoreCacheType.REDIS,
        redis_uri=Cache.REDIS_URI,
        cache_prefix=Cache.PREFIX_KEY,
        redis_cluster_uri=Cache.REDIS_CLUSTER_URI,
        redis_type=Cache.REDIS_TYPE
    )
else:
    lru_redis_cache = LruCache(
        store_type=StoreCacheType.REDIS,
        redis_uri=Cache.REDIS_URI,
        cache_prefix=Cache.PREFIX_KEY,
    )
