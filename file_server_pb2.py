# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_server.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='file_server.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11\x66ile_server.proto\"\x16\n\x05\x43hunk\x12\r\n\x05\x63hunk\x18\x01 \x01(\x0c\"\x1f\n\x0cUploadStatus\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x32\n\x0b\x46ileService\x12#\n\x06Upload\x12\x06.Chunk\x1a\r.UploadStatus\"\x00(\x01\x62\x06proto3'
)




_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk', full_name='Chunk.chunk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=43,
)


_UPLOADSTATUS = _descriptor.Descriptor(
  name='UploadStatus',
  full_name='UploadStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='UploadStatus.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=45,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['UploadStatus'] = _UPLOADSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'file_server_pb2'
  # @@protoc_insertion_point(class_scope:Chunk)
  })
_sym_db.RegisterMessage(Chunk)

UploadStatus = _reflection.GeneratedProtocolMessageType('UploadStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADSTATUS,
  '__module__' : 'file_server_pb2'
  # @@protoc_insertion_point(class_scope:UploadStatus)
  })
_sym_db.RegisterMessage(UploadStatus)



_FILESERVICE = _descriptor.ServiceDescriptor(
  name='FileService',
  full_name='FileService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=78,
  serialized_end=128,
  methods=[
  _descriptor.MethodDescriptor(
    name='Upload',
    full_name='FileService.Upload',
    index=0,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_UPLOADSTATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['FileService'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)
