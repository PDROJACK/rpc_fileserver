# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fileserver.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import keyDistServer_pb2 as keyDistServer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fileserver.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x66ileserver.proto\x1a\x13keyDistServer.proto\"*\n\x0b\x41uthRequest\x12\x0f\n\x07message\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\x05\"\x10\n\x0e\x43ommandRequest\"\x11\n\x0f\x43ommandResponse2\xc3\x01\n\nFileServer\x12;\n\x0c\x41uthenticate\x12\x0c.AuthRequest\x1a\x1b.keydistserver.AuthResponse\"\x00\x12\x44\n\x15\x41utheticationComplete\x12\x0c.AuthRequest\x1a\x1b.keydistserver.AuthResponse\"\x00\x12\x32\n\x0bTakeCommand\x12\x0f.CommandRequest\x1a\x10.CommandResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[keyDistServer__pb2.DESCRIPTOR,])




_AUTHREQUEST = _descriptor.Descriptor(
  name='AuthRequest',
  full_name='AuthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='AuthRequest.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='AuthRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=41,
  serialized_end=83,
)


_COMMANDREQUEST = _descriptor.Descriptor(
  name='CommandRequest',
  full_name='CommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=85,
  serialized_end=101,
)


_COMMANDRESPONSE = _descriptor.Descriptor(
  name='CommandResponse',
  full_name='CommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=103,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['AuthRequest'] = _AUTHREQUEST
DESCRIPTOR.message_types_by_name['CommandRequest'] = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['CommandResponse'] = _COMMANDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthRequest = _reflection.GeneratedProtocolMessageType('AuthRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQUEST,
  '__module__' : 'fileserver_pb2'
  # @@protoc_insertion_point(class_scope:AuthRequest)
  })
_sym_db.RegisterMessage(AuthRequest)

CommandRequest = _reflection.GeneratedProtocolMessageType('CommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDREQUEST,
  '__module__' : 'fileserver_pb2'
  # @@protoc_insertion_point(class_scope:CommandRequest)
  })
_sym_db.RegisterMessage(CommandRequest)

CommandResponse = _reflection.GeneratedProtocolMessageType('CommandResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDRESPONSE,
  '__module__' : 'fileserver_pb2'
  # @@protoc_insertion_point(class_scope:CommandResponse)
  })
_sym_db.RegisterMessage(CommandResponse)



_FILESERVER = _descriptor.ServiceDescriptor(
  name='FileServer',
  full_name='FileServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=123,
  serialized_end=318,
  methods=[
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='FileServer.Authenticate',
    index=0,
    containing_service=None,
    input_type=_AUTHREQUEST,
    output_type=keyDistServer__pb2._AUTHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AutheticationComplete',
    full_name='FileServer.AutheticationComplete',
    index=1,
    containing_service=None,
    input_type=_AUTHREQUEST,
    output_type=keyDistServer__pb2._AUTHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TakeCommand',
    full_name='FileServer.TakeCommand',
    index=2,
    containing_service=None,
    input_type=_COMMANDREQUEST,
    output_type=_COMMANDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVER)

DESCRIPTOR.services_by_name['FileServer'] = _FILESERVER

# @@protoc_insertion_point(module_scope)