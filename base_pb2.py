# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='base.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nbase.proto\"\x10\n\x03\x63md\x12\t\n\x01\x63\x18\x01 \x01(\x05\";\n\x16\x63lient_gobang_position\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\";\n\x16server_gobang_position\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\"=\n\x0c\x63lient_login\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0e\n\x06passwd\x18\x03 \x01(\t\"?\n\x0cserver_login\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x11\n\tisSuccess\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\"r\n\x0f\x63lient_register\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0e\n\x06passwd\x18\x03 \x01(\t\x12\x0f\n\x07nicheng\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x10\n\x08touxiang\x18\x06 \x01(\t\"B\n\x0fserver_register\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x11\n\tisSuccess\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\"7\n\x12\x63lient_create_game\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x14\n\x0cwithUsername\x18\x02 \x01(\t\"2\n\x13server_online_infor\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0e\n\x06people\x18\x02 \x03(\t\"1\n\x12server_game_invite\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0e\n\x06people\x18\x02 \x01(\t\"/\n\x12\x63lient_game_invite\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"1\n\x14server_game_isInvite\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"#\n\x04test\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0e\n\x06inform\x18\x02 \x01(\t\"D\n\x0b\x63hatMessage\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\x05\"\xbe\x01\n\x11server_user_infor\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08integral\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x10\n\x08numsGame\x18\x05 \x01(\x05\x12\x0b\n\x03win\x18\x06 \x01(\x05\x12\x0c\n\x04lose\x18\x07 \x01(\x05\x12\x0c\n\x04\x64raw\x18\x08 \x01(\x05\x12\x14\n\x0cgameCurrency\x18\t \x01(\x05\x12\x0e\n\x06\x61vatar\x18\n \x01(\t\x12\x0c\n\x04\x63ode\x18\x0b \x01(\x05\"0\n\x06whoWin\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0b\n\x03win\x18\x03 \x01(\t\"%\n\x08withDraw\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04nums\x18\x02 \x01(\x05\"-\n\x10requestResources\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"=\n\x11responseResources\x12\x0b\n\x03\x63md\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\r\n\x05\x63ode2\x18\x03 \x01(\x05\x62\x06proto3'
)




_CMD = _descriptor.Descriptor(
  name='cmd',
  full_name='cmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='cmd.c', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=14,
  serialized_end=30,
)


_CLIENT_GOBANG_POSITION = _descriptor.Descriptor(
  name='client_gobang_position',
  full_name='client_gobang_position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='client_gobang_position.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='client_gobang_position.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='client_gobang_position.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=32,
  serialized_end=91,
)


_SERVER_GOBANG_POSITION = _descriptor.Descriptor(
  name='server_gobang_position',
  full_name='server_gobang_position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='server_gobang_position.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='server_gobang_position.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='server_gobang_position.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=93,
  serialized_end=152,
)


_CLIENT_LOGIN = _descriptor.Descriptor(
  name='client_login',
  full_name='client_login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='client_login.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='client_login.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='client_login.passwd', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=154,
  serialized_end=215,
)


_SERVER_LOGIN = _descriptor.Descriptor(
  name='server_login',
  full_name='server_login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='server_login.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='server_login.isSuccess', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='server_login.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=217,
  serialized_end=280,
)


_CLIENT_REGISTER = _descriptor.Descriptor(
  name='client_register',
  full_name='client_register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='client_register.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='client_register.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passwd', full_name='client_register.passwd', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nicheng', full_name='client_register.nicheng', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='client_register.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='touxiang', full_name='client_register.touxiang', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=282,
  serialized_end=396,
)


_SERVER_REGISTER = _descriptor.Descriptor(
  name='server_register',
  full_name='server_register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='server_register.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSuccess', full_name='server_register.isSuccess', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='server_register.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=398,
  serialized_end=464,
)


_CLIENT_CREATE_GAME = _descriptor.Descriptor(
  name='client_create_game',
  full_name='client_create_game',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='client_create_game.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withUsername', full_name='client_create_game.withUsername', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=466,
  serialized_end=521,
)


_SERVER_ONLINE_INFOR = _descriptor.Descriptor(
  name='server_online_infor',
  full_name='server_online_infor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='server_online_infor.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='people', full_name='server_online_infor.people', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=523,
  serialized_end=573,
)


_SERVER_GAME_INVITE = _descriptor.Descriptor(
  name='server_game_invite',
  full_name='server_game_invite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='server_game_invite.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='people', full_name='server_game_invite.people', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=575,
  serialized_end=624,
)


_CLIENT_GAME_INVITE = _descriptor.Descriptor(
  name='client_game_invite',
  full_name='client_game_invite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='client_game_invite.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='client_game_invite.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=626,
  serialized_end=673,
)


_SERVER_GAME_ISINVITE = _descriptor.Descriptor(
  name='server_game_isInvite',
  full_name='server_game_isInvite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='server_game_isInvite.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='server_game_isInvite.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=675,
  serialized_end=724,
)


_TEST = _descriptor.Descriptor(
  name='test',
  full_name='test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='test.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inform', full_name='test.inform', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=726,
  serialized_end=761,
)


_CHATMESSAGE = _descriptor.Descriptor(
  name='chatMessage',
  full_name='chatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='chatMessage.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='chatMessage.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='chatMessage.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='chatMessage.type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=763,
  serialized_end=831,
)


_SERVER_USER_INFOR = _descriptor.Descriptor(
  name='server_user_infor',
  full_name='server_user_infor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='server_user_infor.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='server_user_infor.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integral', full_name='server_user_infor.integral', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='server_user_infor.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numsGame', full_name='server_user_infor.numsGame', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='win', full_name='server_user_infor.win', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lose', full_name='server_user_infor.lose', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draw', full_name='server_user_infor.draw', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gameCurrency', full_name='server_user_infor.gameCurrency', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='server_user_infor.avatar', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='server_user_infor.code', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=834,
  serialized_end=1024,
)


_WHOWIN = _descriptor.Descriptor(
  name='whoWin',
  full_name='whoWin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='whoWin.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='whoWin.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='win', full_name='whoWin.win', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1026,
  serialized_end=1074,
)


_WITHDRAW = _descriptor.Descriptor(
  name='withDraw',
  full_name='withDraw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='withDraw.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nums', full_name='withDraw.nums', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1076,
  serialized_end=1113,
)


_REQUESTRESOURCES = _descriptor.Descriptor(
  name='requestResources',
  full_name='requestResources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='requestResources.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='requestResources.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1115,
  serialized_end=1160,
)


_RESPONSERESOURCES = _descriptor.Descriptor(
  name='responseResources',
  full_name='responseResources',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='responseResources.cmd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='responseResources.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code2', full_name='responseResources.code2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1162,
  serialized_end=1223,
)

DESCRIPTOR.message_types_by_name['cmd'] = _CMD
DESCRIPTOR.message_types_by_name['client_gobang_position'] = _CLIENT_GOBANG_POSITION
DESCRIPTOR.message_types_by_name['server_gobang_position'] = _SERVER_GOBANG_POSITION
DESCRIPTOR.message_types_by_name['client_login'] = _CLIENT_LOGIN
DESCRIPTOR.message_types_by_name['server_login'] = _SERVER_LOGIN
DESCRIPTOR.message_types_by_name['client_register'] = _CLIENT_REGISTER
DESCRIPTOR.message_types_by_name['server_register'] = _SERVER_REGISTER
DESCRIPTOR.message_types_by_name['client_create_game'] = _CLIENT_CREATE_GAME
DESCRIPTOR.message_types_by_name['server_online_infor'] = _SERVER_ONLINE_INFOR
DESCRIPTOR.message_types_by_name['server_game_invite'] = _SERVER_GAME_INVITE
DESCRIPTOR.message_types_by_name['client_game_invite'] = _CLIENT_GAME_INVITE
DESCRIPTOR.message_types_by_name['server_game_isInvite'] = _SERVER_GAME_ISINVITE
DESCRIPTOR.message_types_by_name['test'] = _TEST
DESCRIPTOR.message_types_by_name['chatMessage'] = _CHATMESSAGE
DESCRIPTOR.message_types_by_name['server_user_infor'] = _SERVER_USER_INFOR
DESCRIPTOR.message_types_by_name['whoWin'] = _WHOWIN
DESCRIPTOR.message_types_by_name['withDraw'] = _WITHDRAW
DESCRIPTOR.message_types_by_name['requestResources'] = _REQUESTRESOURCES
DESCRIPTOR.message_types_by_name['responseResources'] = _RESPONSERESOURCES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

cmd = _reflection.GeneratedProtocolMessageType('cmd', (_message.Message,), {
  'DESCRIPTOR': _CMD,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:cmd)
})
_sym_db.RegisterMessage(cmd)

client_gobang_position = _reflection.GeneratedProtocolMessageType('client_gobang_position', (_message.Message,), {
  'DESCRIPTOR': _CLIENT_GOBANG_POSITION,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:client_gobang_position)
})
_sym_db.RegisterMessage(client_gobang_position)

server_gobang_position = _reflection.GeneratedProtocolMessageType('server_gobang_position', (_message.Message,), {
  'DESCRIPTOR': _SERVER_GOBANG_POSITION,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:server_gobang_position)
})
_sym_db.RegisterMessage(server_gobang_position)

client_login = _reflection.GeneratedProtocolMessageType('client_login', (_message.Message,), {
  'DESCRIPTOR': _CLIENT_LOGIN,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:client_login)
})
_sym_db.RegisterMessage(client_login)

server_login = _reflection.GeneratedProtocolMessageType('server_login', (_message.Message,), {
  'DESCRIPTOR': _SERVER_LOGIN,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:server_login)
})
_sym_db.RegisterMessage(server_login)

client_register = _reflection.GeneratedProtocolMessageType('client_register', (_message.Message,), {
  'DESCRIPTOR': _CLIENT_REGISTER,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:client_register)
})
_sym_db.RegisterMessage(client_register)

server_register = _reflection.GeneratedProtocolMessageType('server_register', (_message.Message,), {
  'DESCRIPTOR': _SERVER_REGISTER,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:server_register)
})
_sym_db.RegisterMessage(server_register)

client_create_game = _reflection.GeneratedProtocolMessageType('client_create_game', (_message.Message,), {
  'DESCRIPTOR': _CLIENT_CREATE_GAME,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:client_create_game)
})
_sym_db.RegisterMessage(client_create_game)

server_online_infor = _reflection.GeneratedProtocolMessageType('server_online_infor', (_message.Message,), {
  'DESCRIPTOR': _SERVER_ONLINE_INFOR,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:server_online_infor)
})
_sym_db.RegisterMessage(server_online_infor)

server_game_invite = _reflection.GeneratedProtocolMessageType('server_game_invite', (_message.Message,), {
  'DESCRIPTOR': _SERVER_GAME_INVITE,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:server_game_invite)
})
_sym_db.RegisterMessage(server_game_invite)

client_game_invite = _reflection.GeneratedProtocolMessageType('client_game_invite', (_message.Message,), {
  'DESCRIPTOR': _CLIENT_GAME_INVITE,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:client_game_invite)
})
_sym_db.RegisterMessage(client_game_invite)

server_game_isInvite = _reflection.GeneratedProtocolMessageType('server_game_isInvite', (_message.Message,), {
  'DESCRIPTOR': _SERVER_GAME_ISINVITE,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:server_game_isInvite)
})
_sym_db.RegisterMessage(server_game_isInvite)

test = _reflection.GeneratedProtocolMessageType('test', (_message.Message,), {
  'DESCRIPTOR': _TEST,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:test)
})
_sym_db.RegisterMessage(test)

chatMessage = _reflection.GeneratedProtocolMessageType('chatMessage', (_message.Message,), {
  'DESCRIPTOR': _CHATMESSAGE,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:chatMessage)
})
_sym_db.RegisterMessage(chatMessage)

server_user_infor = _reflection.GeneratedProtocolMessageType('server_user_infor', (_message.Message,), {
  'DESCRIPTOR': _SERVER_USER_INFOR,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:server_user_infor)
})
_sym_db.RegisterMessage(server_user_infor)

whoWin = _reflection.GeneratedProtocolMessageType('whoWin', (_message.Message,), {
  'DESCRIPTOR': _WHOWIN,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:whoWin)
})
_sym_db.RegisterMessage(whoWin)

withDraw = _reflection.GeneratedProtocolMessageType('withDraw', (_message.Message,), {
  'DESCRIPTOR': _WITHDRAW,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:withDraw)
})
_sym_db.RegisterMessage(withDraw)

requestResources = _reflection.GeneratedProtocolMessageType('requestResources', (_message.Message,), {
  'DESCRIPTOR': _REQUESTRESOURCES,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:requestResources)
})
_sym_db.RegisterMessage(requestResources)

responseResources = _reflection.GeneratedProtocolMessageType('responseResources', (_message.Message,), {
  'DESCRIPTOR': _RESPONSERESOURCES,
  '__module__': 'base_pb2'
  # @@protoc_insertion_point(class_scope:responseResources)
})
_sym_db.RegisterMessage(responseResources)

# @@protoc_insertion_point(module_scope)
