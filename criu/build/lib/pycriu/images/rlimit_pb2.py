# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rlimit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rlimit.proto',
  package='',
  serialized_pb=_b('\n\x0crlimit.proto\"(\n\x0crlimit_entry\x12\x0b\n\x03\x63ur\x18\x01 \x02(\x04\x12\x0b\n\x03max\x18\x02 \x02(\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RLIMIT_ENTRY = _descriptor.Descriptor(
  name='rlimit_entry',
  full_name='rlimit_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cur', full_name='rlimit_entry.cur', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='rlimit_entry.max', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=56,
)

DESCRIPTOR.message_types_by_name['rlimit_entry'] = _RLIMIT_ENTRY

rlimit_entry = _reflection.GeneratedProtocolMessageType('rlimit_entry', (_message.Message,), dict(
  DESCRIPTOR = _RLIMIT_ENTRY,
  __module__ = 'rlimit_pb2'
  # @@protoc_insertion_point(class_scope:rlimit_entry)
  ))
_sym_db.RegisterMessage(rlimit_entry)


# @@protoc_insertion_point(module_scope)
