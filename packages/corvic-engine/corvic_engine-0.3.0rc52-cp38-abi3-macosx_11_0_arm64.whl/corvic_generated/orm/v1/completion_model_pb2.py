# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corvic/orm/v1/completion_model.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$corvic/orm/v1/completion_model.proto\x12\rcorvic.orm.v1\"S\n\x17GenericOpenAIParameters\x12\x1d\n\nmodel_name\x18\x01 \x01(\tR\tmodelName\x12\x19\n\x08\x62\x61se_url\x18\x02 \x01(\tR\x07\x62\x61seUrl\"\x9d\x01\n\x15\x41zureOpenAIParameters\x12\x19\n\x08\x62\x61se_url\x18\x01 \x01(\tR\x07\x62\x61seUrl\x12#\n\rresource_name\x18\x02 \x01(\tR\x0cresourceName\x12#\n\rdeployment_id\x18\x03 \x01(\tR\x0c\x64\x65ploymentId\x12\x1f\n\x0b\x61pi_version\x18\x04 \x01(\tR\napiVersion\"\xeb\x01\n\x19\x43ompletionModelParameters\x12\x64\n\x19generic_openai_parameters\x18\x01 \x01(\x0b\x32&.corvic.orm.v1.GenericOpenAIParametersH\x00R\x17genericOpenaiParameters\x12^\n\x17\x61zure_openai_parameters\x18\x02 \x01(\x0b\x32$.corvic.orm.v1.AzureOpenAIParametersH\x00R\x15\x61zureOpenaiParametersB\x08\n\x06paramsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'corvic.orm.v1.completion_model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GENERICOPENAIPARAMETERS']._serialized_start=55
  _globals['_GENERICOPENAIPARAMETERS']._serialized_end=138
  _globals['_AZUREOPENAIPARAMETERS']._serialized_start=141
  _globals['_AZUREOPENAIPARAMETERS']._serialized_end=298
  _globals['_COMPLETIONMODELPARAMETERS']._serialized_start=301
  _globals['_COMPLETIONMODELPARAMETERS']._serialized_end=536
# @@protoc_insertion_point(module_scope)
