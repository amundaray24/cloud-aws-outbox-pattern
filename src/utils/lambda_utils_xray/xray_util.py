from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

def _get_trace_id():
    return xray_recorder.current_segment().trace_id if xray_recorder.current_segment() else 'NoTrace'

def _get_span_id():
    return xray_recorder.current_subsegment().id if xray_recorder.current_subsegment() else 'NoSpan'

def get_trace_info():
    return {
        "trace_id": _get_trace_id(),
        "span_id": _get_span_id()
    }

def create_new_subsegment(name):
    return xray_recorder.begin_subsegment(name)

def end_subsegment():
    xray_recorder.end_subsegment()
