# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keyDistServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='keyDistServer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13keyDistServer.proto\"\"\n\x04Info\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\" \n\x05\x43reds\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\"\'\n\x14\x41uthRequestEncrypted\x12\x0f\n\x07message\x18\x01 \x01(\t\"T\n\x14\x41uthRequestDecrypted\x12\r\n\x05myKey\x18\x01 \x01(\t\x12\x0c\n\x04myId\x18\x02 \x01(\x05\x12\x10\n\x08targetId\x18\x03 \x01(\x05\x12\r\n\x05nonce\x18\x04 \x01(\x05\"\x1f\n\x0c\x41uthResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\r\n\x0bInfoRequest\"+\n\x0f\x46ileServerEntry\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04port\x18\x02 \x01(\t\"6\n\x0cInfoResponse\x12&\n\x0c\x66ile_servers\x18\x01 \x03(\x0b\x32\x10.FileServerEntry2\x90\x01\n\x07\x43onnect\x12\x1d\n\nConnectNew\x12\x05.Info\x1a\x06.Creds\"\x00\x12\x36\n\x0c\x41uthenticate\x12\x15.AuthRequestEncrypted\x1a\r.AuthResponse\"\x00\x12.\n\rGetServerInfo\x12\x0c.InfoRequest\x1a\r.InfoResponse\"\x00\x62\x06proto3'
)




_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Info.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='Info.port', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=23,
  serialized_end=57,
)


_CREDS = _descriptor.Descriptor(
  name='Creds',
  full_name='Creds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Creds.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='Creds.id', index=1,
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
  serialized_start=59,
  serialized_end=91,
)


_AUTHREQUESTENCRYPTED = _descriptor.Descriptor(
  name='AuthRequestEncrypted',
  full_name='AuthRequestEncrypted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='AuthRequestEncrypted.message', index=0,
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
  serialized_start=93,
  serialized_end=132,
)


_AUTHREQUESTDECRYPTED = _descriptor.Descriptor(
  name='AuthRequestDecrypted',
  full_name='AuthRequestDecrypted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='myKey', full_name='AuthRequestDecrypted.myKey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='myId', full_name='AuthRequestDecrypted.myId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetId', full_name='AuthRequestDecrypted.targetId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='AuthRequestDecrypted.nonce', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=134,
  serialized_end=218,
)


_AUTHRESPONSE = _descriptor.Descriptor(
  name='AuthResponse',
  full_name='AuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='AuthResponse.message', index=0,
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
  serialized_start=220,
  serialized_end=251,
)


_INFOREQUEST = _descriptor.Descriptor(
  name='InfoRequest',
  full_name='InfoRequest',
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
  serialized_start=253,
  serialized_end=266,
)


_FILESERVERENTRY = _descriptor.Descriptor(
  name='FileServerEntry',
  full_name='FileServerEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='FileServerEntry.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='FileServerEntry.port', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=268,
  serialized_end=311,
)


_INFORESPONSE = _descriptor.Descriptor(
  name='InfoResponse',
  full_name='InfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_servers', full_name='InfoResponse.file_servers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=313,
  serialized_end=367,
)

_INFORESPONSE.fields_by_name['file_servers'].message_type = _FILESERVERENTRY
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['Creds'] = _CREDS
DESCRIPTOR.message_types_by_name['AuthRequestEncrypted'] = _AUTHREQUESTENCRYPTED
DESCRIPTOR.message_types_by_name['AuthRequestDecrypted'] = _AUTHREQUESTDECRYPTED
DESCRIPTOR.message_types_by_name['AuthResponse'] = _AUTHRESPONSE
DESCRIPTOR.message_types_by_name['InfoRequest'] = _INFOREQUEST
DESCRIPTOR.message_types_by_name['FileServerEntry'] = _FILESERVERENTRY
DESCRIPTOR.message_types_by_name['InfoResponse'] = _INFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), {
  'DESCRIPTOR' : _INFO,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:Info)
  })
_sym_db.RegisterMessage(Info)

Creds = _reflection.GeneratedProtocolMessageType('Creds', (_message.Message,), {
  'DESCRIPTOR' : _CREDS,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:Creds)
  })
_sym_db.RegisterMessage(Creds)

AuthRequestEncrypted = _reflection.GeneratedProtocolMessageType('AuthRequestEncrypted', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQUESTENCRYPTED,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:AuthRequestEncrypted)
  })
_sym_db.RegisterMessage(AuthRequestEncrypted)

AuthRequestDecrypted = _reflection.GeneratedProtocolMessageType('AuthRequestDecrypted', (_message.Message,), {
  'DESCRIPTOR' : _AUTHREQUESTDECRYPTED,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:AuthRequestDecrypted)
  })
_sym_db.RegisterMessage(AuthRequestDecrypted)

AuthResponse = _reflection.GeneratedProtocolMessageType('AuthResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHRESPONSE,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:AuthResponse)
  })
_sym_db.RegisterMessage(AuthResponse)

InfoRequest = _reflection.GeneratedProtocolMessageType('InfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _INFOREQUEST,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:InfoRequest)
  })
_sym_db.RegisterMessage(InfoRequest)

FileServerEntry = _reflection.GeneratedProtocolMessageType('FileServerEntry', (_message.Message,), {
  'DESCRIPTOR' : _FILESERVERENTRY,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:FileServerEntry)
  })
_sym_db.RegisterMessage(FileServerEntry)

InfoResponse = _reflection.GeneratedProtocolMessageType('InfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _INFORESPONSE,
  '__module__' : 'keyDistServer_pb2'
  # @@protoc_insertion_point(class_scope:InfoResponse)
  })
_sym_db.RegisterMessage(InfoResponse)



_CONNECT = _descriptor.ServiceDescriptor(
  name='Connect',
  full_name='Connect',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=370,
  serialized_end=514,
  methods=[
  _descriptor.MethodDescriptor(
    name='ConnectNew',
    full_name='Connect.ConnectNew',
    index=0,
    containing_service=None,
    input_type=_INFO,
    output_type=_CREDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Authenticate',
    full_name='Connect.Authenticate',
    index=1,
    containing_service=None,
    input_type=_AUTHREQUESTENCRYPTED,
    output_type=_AUTHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServerInfo',
    full_name='Connect.GetServerInfo',
    index=2,
    containing_service=None,
    input_type=_INFOREQUEST,
    output_type=_INFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECT)

DESCRIPTOR.services_by_name['Connect'] = _CONNECT

# @@protoc_insertion_point(module_scope)