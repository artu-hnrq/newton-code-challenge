# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculate.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculate.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63\x61lculate.proto\"\x97\x01\n\x0b\x43\x61lculation\x12)\n\toperation\x18\x01 \x02(\x0e\x32\x16.Calculation.Operation\x12\x0e\n\x06number\x18\x02 \x03(\x05\"M\n\tOperation\x12\r\n\tADDICTION\x10\x00\x12\x0f\n\x0bSUBTRACTION\x10\x01\x12\x12\n\x0eMULTIPLICATION\x10\x02\x12\x0c\n\x08\x44IVISION\x10\x03\"\x1a\n\x05Ready\x12\x11\n\tclient_id\x18\x01 \x01(\x05\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t2V\n\x0bTaskManager\x12$\n\x07Request\x12\x0c.Calculation\x1a\t.Response\"\x00\x12!\n\x07GetTask\x12\x06.Ready\x1a\x0c.Calculation\"\x00'
)



_CALCULATION_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='Calculation.Operation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADDICTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUBTRACTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLICATION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIVISION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=94,
  serialized_end=171,
)
_sym_db.RegisterEnumDescriptor(_CALCULATION_OPERATION)


_CALCULATION = _descriptor.Descriptor(
  name='Calculation',
  full_name='Calculation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Calculation.operation', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='Calculation.number', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CALCULATION_OPERATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=171,
)


_READY = _descriptor.Descriptor(
  name='Ready',
  full_name='Ready',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='Ready.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=199,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Response.message', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=228,
)

_CALCULATION.fields_by_name['operation'].enum_type = _CALCULATION_OPERATION
_CALCULATION_OPERATION.containing_type = _CALCULATION
DESCRIPTOR.message_types_by_name['Calculation'] = _CALCULATION
DESCRIPTOR.message_types_by_name['Ready'] = _READY
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Calculation = _reflection.GeneratedProtocolMessageType('Calculation', (_message.Message,), {
  'DESCRIPTOR' : _CALCULATION,
  '__module__' : 'calculate_pb2'
  # @@protoc_insertion_point(class_scope:Calculation)
  })
_sym_db.RegisterMessage(Calculation)

Ready = _reflection.GeneratedProtocolMessageType('Ready', (_message.Message,), {
  'DESCRIPTOR' : _READY,
  '__module__' : 'calculate_pb2'
  # @@protoc_insertion_point(class_scope:Ready)
  })
_sym_db.RegisterMessage(Ready)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'calculate_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)



_TASKMANAGER = _descriptor.ServiceDescriptor(
  name='TaskManager',
  full_name='TaskManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=230,
  serialized_end=316,
  methods=[
  _descriptor.MethodDescriptor(
    name='Request',
    full_name='TaskManager.Request',
    index=0,
    containing_service=None,
    input_type=_CALCULATION,
    output_type=_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTask',
    full_name='TaskManager.GetTask',
    index=1,
    containing_service=None,
    input_type=_READY,
    output_type=_CALCULATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKMANAGER)

DESCRIPTOR.services_by_name['TaskManager'] = _TASKMANAGER

# @@protoc_insertion_point(module_scope)