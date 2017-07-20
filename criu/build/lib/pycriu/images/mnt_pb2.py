# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mnt.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import opts_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mnt.proto',
  package='',
  serialized_pb=_b('\n\tmnt.proto\x1a\nopts.proto\"\xe7\x02\n\tmnt_entry\x12\x0e\n\x06\x66stype\x18\x01 \x02(\r\x12\x0e\n\x06mnt_id\x18\x02 \x02(\r\x12\x17\n\x08root_dev\x18\x03 \x02(\rB\x05\xd2?\x02 \x01\x12\x15\n\rparent_mnt_id\x18\x04 \x02(\r\x12\x14\n\x05\x66lags\x18\x05 \x02(\rB\x05\xd2?\x02\x08\x01\x12\x0c\n\x04root\x18\x06 \x02(\t\x12\x12\n\nmountpoint\x18\x07 \x02(\t\x12\x0e\n\x06source\x18\x08 \x02(\t\x12\x0f\n\x07options\x18\t \x02(\t\x12\x11\n\tshared_id\x18\n \x01(\r\x12\x11\n\tmaster_id\x18\x0b \x01(\r\x12\x13\n\x0bwith_plugin\x18\x0c \x01(\x08\x12\x11\n\text_mount\x18\r \x01(\x08\x12\x0e\n\x06\x66sname\x18\x0e \x01(\t\x12\x18\n\x10internal_sharing\x18\x0f \x01(\x08\x12\x0f\n\x07\x64\x65leted\x18\x10 \x01(\x08\x12\x17\n\x08sb_flags\x18\x11 \x01(\rB\x05\xd2?\x02\x08\x01\x12\x0f\n\x07\x65xt_key\x18\x12 \x01(\t*\x83\x02\n\x06\x66stype\x12\x0f\n\x0bUNSUPPORTED\x10\x00\x12\x08\n\x04PROC\x10\x01\x12\t\n\x05SYSFS\x10\x02\x12\x0c\n\x08\x44\x45VTMPFS\x10\x03\x12\x0f\n\x0b\x42INFMT_MISC\x10\x04\x12\t\n\x05TMPFS\x10\x05\x12\n\n\x06\x44\x45VPTS\x10\x06\x12\t\n\x05SIMFS\x10\x07\x12\n\n\x06PSTORE\x10\x08\x12\x0e\n\nSECURITYFS\x10\t\x12\x0b\n\x07\x46USECTL\x10\n\x12\x0b\n\x07\x44\x45\x42UGFS\x10\x0b\x12\n\n\x06\x43GROUP\x10\x0c\x12\x08\n\x04\x41UFS\x10\r\x12\n\n\x06MQUEUE\x10\x0e\x12\x08\n\x04\x46USE\x10\x0f\x12\x08\n\x04\x41UTO\x10\x10\x12\r\n\tOVERLAYFS\x10\x11\x12\n\n\x06\x41UTOFS\x10\x12\x12\x0b\n\x07TRACEFS\x10\x13')
  ,
  dependencies=[opts_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FSTYPE = _descriptor.EnumDescriptor(
  name='fstype',
  full_name='fstype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSFS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVTMPFS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINFMT_MISC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TMPFS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVPTS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIMFS', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PSTORE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECURITYFS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUSECTL', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUGFS', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CGROUP', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUFS', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MQUEUE', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUSE', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAYFS', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOFS', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACEFS', index=19, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=388,
  serialized_end=647,
)
_sym_db.RegisterEnumDescriptor(_FSTYPE)

fstype = enum_type_wrapper.EnumTypeWrapper(_FSTYPE)
UNSUPPORTED = 0
PROC = 1
SYSFS = 2
DEVTMPFS = 3
BINFMT_MISC = 4
TMPFS = 5
DEVPTS = 6
SIMFS = 7
PSTORE = 8
SECURITYFS = 9
FUSECTL = 10
DEBUGFS = 11
CGROUP = 12
AUFS = 13
MQUEUE = 14
FUSE = 15
AUTO = 16
OVERLAYFS = 17
AUTOFS = 18
TRACEFS = 19



_MNT_ENTRY = _descriptor.Descriptor(
  name='mnt_entry',
  full_name='mnt_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fstype', full_name='mnt_entry.fstype', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mnt_id', full_name='mnt_entry.mnt_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root_dev', full_name='mnt_entry.root_dev', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002 \001'))),
    _descriptor.FieldDescriptor(
      name='parent_mnt_id', full_name='mnt_entry.parent_mnt_id', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='mnt_entry.flags', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='root', full_name='mnt_entry.root', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mountpoint', full_name='mnt_entry.mountpoint', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='mnt_entry.source', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='mnt_entry.options', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shared_id', full_name='mnt_entry.shared_id', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='master_id', full_name='mnt_entry.master_id', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_plugin', full_name='mnt_entry.with_plugin', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ext_mount', full_name='mnt_entry.ext_mount', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fsname', full_name='mnt_entry.fsname', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='internal_sharing', full_name='mnt_entry.internal_sharing', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='mnt_entry.deleted', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sb_flags', full_name='mnt_entry.sb_flags', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='ext_key', full_name='mnt_entry.ext_key', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=26,
  serialized_end=385,
)

DESCRIPTOR.message_types_by_name['mnt_entry'] = _MNT_ENTRY
DESCRIPTOR.enum_types_by_name['fstype'] = _FSTYPE

mnt_entry = _reflection.GeneratedProtocolMessageType('mnt_entry', (_message.Message,), dict(
  DESCRIPTOR = _MNT_ENTRY,
  __module__ = 'mnt_pb2'
  # @@protoc_insertion_point(class_scope:mnt_entry)
  ))
_sym_db.RegisterMessage(mnt_entry)


_MNT_ENTRY.fields_by_name['root_dev'].has_options = True
_MNT_ENTRY.fields_by_name['root_dev']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002 \001'))
_MNT_ENTRY.fields_by_name['flags'].has_options = True
_MNT_ENTRY.fields_by_name['flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MNT_ENTRY.fields_by_name['sb_flags'].has_options = True
_MNT_ENTRY.fields_by_name['sb_flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
# @@protoc_insertion_point(module_scope)
