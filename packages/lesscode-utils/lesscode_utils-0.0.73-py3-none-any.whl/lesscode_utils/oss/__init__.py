from lesscode_utils.oss.aliyun_oss import AliYunOss
from lesscode_utils.oss.ks3_oss import Ks3Oss


class CommonOss:
    def __init__(self, storage_type, **kwargs):
        """
        初始化OSS
        Args:
            storage_type (str): 存储类型，目前支持ks3和aliyun
        """
        self.storage_type = storage_type
        self.storage_config = kwargs.get("storage_config", {})
        if self.storage_type == "ks3":
            self.storage_instance = Ks3Oss(**self.storage_config)
        elif self.storage_type == "aliyun":
            self.storage_instance = AliYunOss(**self.storage_config)
        else:
            raise Exception("storage_type is not support")

    def __getattr__(self, item):
        return getattr(self.storage_instance, item)
