# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: transport.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'transport.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftransport.proto\x12\ttransport\">\n\x11\x42usArrivalRequest\x12\x15\n\rbus_stop_code\x18\x01 \x01(\t\x12\x12\n\nservice_no\x18\x02 \x01(\t\"\x7f\n\x12\x42usArrivalResponse\x12\x12\n\nservice_no\x18\x01 \x01(\t\x12\x19\n\x11next_arrival_time\x18\x02 \x01(\t\x12\x1a\n\x12next_arrival_time2\x18\x03 \x01(\t\x12\x0c\n\x04load\x18\x04 \x01(\t\x12\x10\n\x08\x62us_type\x18\x05 \x01(\t\"-\n\x11\x42usServiceRequest\x12\x18\n\x10\x62us_service_code\x18\x01 \x01(\t\"{\n\x12\x42usServiceResponse\x12\x16\n\x0e\x62us_service_no\x18\x01 \x01(\t\x12\x13\n\x0borigin_name\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65stination_name\x18\x03 \x01(\t\x12\x0c\n\x04loop\x18\x04 \x01(\t\x12\x10\n\x08operator\x18\x05 \x01(\t2\xb1\x01\n\x0fPublicTransport\x12L\n\rGetBusArrival\x12\x1c.transport.BusArrivalRequest\x1a\x1d.transport.BusArrivalResponse\x12P\n\x11GetBusServiceInfo\x12\x1c.transport.BusServiceRequest\x1a\x1d.transport.BusServiceResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BUSARRIVALREQUEST']._serialized_start=30
  _globals['_BUSARRIVALREQUEST']._serialized_end=92
  _globals['_BUSARRIVALRESPONSE']._serialized_start=94
  _globals['_BUSARRIVALRESPONSE']._serialized_end=221
  _globals['_BUSSERVICEREQUEST']._serialized_start=223
  _globals['_BUSSERVICEREQUEST']._serialized_end=268
  _globals['_BUSSERVICERESPONSE']._serialized_start=270
  _globals['_BUSSERVICERESPONSE']._serialized_end=393
  _globals['_PUBLICTRANSPORT']._serialized_start=396
  _globals['_PUBLICTRANSPORT']._serialized_end=573
# @@protoc_insertion_point(module_scope)
