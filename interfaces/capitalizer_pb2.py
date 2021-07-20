# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: capitalizer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='capitalizer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63\x61pitalizer.proto\" \n\rStringRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0eStringResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x96\x01\n\x0b\x43\x61pitalizer\x12/\n\nCapitalize\x12\x0e.StringRequest\x1a\x0f.StringResponse\"\x00\x12*\n\x05Upper\x12\x0e.StringRequest\x1a\x0f.StringResponse\"\x00\x12*\n\x05Lower\x12\x0e.StringRequest\x1a\x0f.StringResponse\"\x00\x62\x06proto3'
)




_STRINGREQUEST = _descriptor.Descriptor(
  name='StringRequest',
  full_name='StringRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='StringRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=53,
)


_STRINGRESPONSE = _descriptor.Descriptor(
  name='StringResponse',
  full_name='StringResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='StringResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['StringRequest'] = _STRINGREQUEST
DESCRIPTOR.message_types_by_name['StringResponse'] = _STRINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringRequest = _reflection.GeneratedProtocolMessageType('StringRequest', (_message.Message,), {
  'DESCRIPTOR' : _STRINGREQUEST,
  '__module__' : 'capitalizer_pb2'
  # @@protoc_insertion_point(class_scope:StringRequest)
  })
_sym_db.RegisterMessage(StringRequest)

StringResponse = _reflection.GeneratedProtocolMessageType('StringResponse', (_message.Message,), {
  'DESCRIPTOR' : _STRINGRESPONSE,
  '__module__' : 'capitalizer_pb2'
  # @@protoc_insertion_point(class_scope:StringResponse)
  })
_sym_db.RegisterMessage(StringResponse)



_CAPITALIZER = _descriptor.ServiceDescriptor(
  name='Capitalizer',
  full_name='Capitalizer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=91,
  serialized_end=241,
  methods=[
  _descriptor.MethodDescriptor(
    name='Capitalize',
    full_name='Capitalizer.Capitalize',
    index=0,
    containing_service=None,
    input_type=_STRINGREQUEST,
    output_type=_STRINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Upper',
    full_name='Capitalizer.Upper',
    index=1,
    containing_service=None,
    input_type=_STRINGREQUEST,
    output_type=_STRINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Lower',
    full_name='Capitalizer.Lower',
    index=2,
    containing_service=None,
    input_type=_STRINGREQUEST,
    output_type=_STRINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CAPITALIZER)

DESCRIPTOR.services_by_name['Capitalizer'] = _CAPITALIZER

# @@protoc_insertion_point(module_scope)