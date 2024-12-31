import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

class XRayFormatter(logging.Formatter):

  def format(self, record):
    trace_id = xray_recorder.current_segment().trace_id if xray_recorder.current_segment() else 'NoTrace'
    span_id = xray_recorder.current_subsegment().id if xray_recorder.current_subsegment() else 'NoSpan'
    record.trace_id = trace_id
    record.span_id = span_id
    return super().format(record)
