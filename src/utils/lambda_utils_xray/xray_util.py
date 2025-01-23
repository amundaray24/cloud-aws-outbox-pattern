from aws_xray_sdk.core import xray_recorder
from lambda_utils_xray.xray_manager import AWSXRayManager

class XRayUtil:

  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(XRayUtil, cls).__new__(cls, *args, **kwargs)
      cls._instance._init()
    return cls._instance

  def _init(self):
    AWSXRayManager()

  @staticmethod
  def get_trace_id():
    segment = xray_recorder.current_segment()
    return segment.trace_id if segment else 'NoTrace'

  @staticmethod
  def get_span_id():
    subsegment = xray_recorder.current_subsegment()
    return subsegment.id if subsegment else 'NoSpan'

  @staticmethod
  def get_trace_info():
    return {
      "trace_id": XRayUtil.get_trace_id(),
      "span_id": XRayUtil.get_span_id()
    }

  @staticmethod
  def create_new_subsegment(name):
    return xray_recorder.begin_subsegment(name)

  @staticmethod
  def end_subsegment():
    xray_recorder.end_subsegment()