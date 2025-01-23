from aws_xray_sdk.core import patch_all

class AWSXRayManager:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
        cls._instance = super(AWSXRayManager, cls).__new__(cls, *args, **kwargs)
        cls._instance._init()
    return cls._instance

  def _init(self):
    patch_all()