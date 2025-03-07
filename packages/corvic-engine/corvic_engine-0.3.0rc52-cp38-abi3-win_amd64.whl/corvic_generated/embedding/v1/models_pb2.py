# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corvic/embedding/v1/models.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n corvic/embedding/v1/models.proto\x12\x13\x63orvic.embedding.v1\"R\n\nParameters\x12\x30\n\x05model\x18\x01 \x01(\x0e\x32\x1a.corvic.embedding.v1.ModelR\x05model\x12\x12\n\x04ndim\x18\x02 \x01(\x05R\x04ndim\"\xf4\x01\n\x19\x43olumnEmbeddingParameters\x12q\n\x11\x63olumn_parameters\x18\x01 \x03(\x0b\x32\x44.corvic.embedding.v1.ColumnEmbeddingParameters.ColumnParametersEntryR\x10\x63olumnParameters\x1a\x64\n\x15\x43olumnParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.corvic.embedding.v1.ParametersR\x05value:\x02\x38\x01\"\x8f\x01\n\x1e\x43oncatStringAndEmbedParameters\x12!\n\x0c\x63olumn_names\x18\x01 \x03(\tR\x0b\x63olumnNames\x12J\n\x10model_parameters\x18\x02 \x01(\x0b\x32\x1f.corvic.embedding.v1.ParametersR\x0fmodelParameters\"\x89\x01\n\x18\x43oncatAndEmbedParameters\x12!\n\x0c\x63olumn_names\x18\x01 \x03(\tR\x0b\x63olumnNames\x12J\n\x10model_parameters\x18\x02 \x01(\x0b\x32\x1f.corvic.embedding.v1.ParametersR\x0fmodelParameters\".\n\x18\x45mbedAndConcatParameters\x12\x12\n\x04ndim\x18\x01 \x01(\x05R\x04ndim\"a\n\x14ImageModelParameters\x12\x35\n\x05model\x18\x01 \x01(\x0e\x32\x1f.corvic.embedding.v1.ImageModelR\x05model\x12\x12\n\x04ndim\x18\x02 \x01(\x05R\x04ndim\"\x8d\x01\n\x14\x45mbedImageParameters\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12T\n\x10model_parameters\x18\x02 \x01(\x0b\x32).corvic.embedding.v1.ImageModelParametersR\x0fmodelParameters*\xdc\x01\n\x05Model\x12\x15\n\x11MODEL_UNSPECIFIED\x10\x00\x12\"\n\x1aMODEL_SENTENCE_TRANSFORMER\x10\x01\x1a\x02\x08\x01\x12\'\n#MODEL_OPENAI_TEXT_EMBEDDING_3_SMALL\x10\x03\x12\'\n#MODEL_OPENAI_TEXT_EMBEDDING_3_LARGE\x10\x04\x12 \n\x1cMODEL_GCP_TEXT_EMBEDDING_004\x10\x05\x12\x10\n\x0cMODEL_CUSTOM\x10\x02\x12\x12\n\x0eMODEL_IDENTITY\x10\x06*q\n\nImageModel\x12\x1b\n\x17IMAGE_MODEL_UNSPECIFIED\x10\x00\x12\x14\n\x10IMAGE_MODEL_CLIP\x10\x01\x12\x16\n\x12IMAGE_MODEL_CUSTOM\x10\x02\x12\x18\n\x14IMAGE_MODEL_IDENTITY\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'corvic.embedding.v1.models_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MODEL'].values_by_name["MODEL_SENTENCE_TRANSFORMER"]._options = None
  _globals['_MODEL'].values_by_name["MODEL_SENTENCE_TRANSFORMER"]._serialized_options = b'\010\001'
  _globals['_COLUMNEMBEDDINGPARAMETERS_COLUMNPARAMETERSENTRY']._options = None
  _globals['_COLUMNEMBEDDINGPARAMETERS_COLUMNPARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_MODEL']._serialized_start=966
  _globals['_MODEL']._serialized_end=1186
  _globals['_IMAGEMODEL']._serialized_start=1188
  _globals['_IMAGEMODEL']._serialized_end=1301
  _globals['_PARAMETERS']._serialized_start=57
  _globals['_PARAMETERS']._serialized_end=139
  _globals['_COLUMNEMBEDDINGPARAMETERS']._serialized_start=142
  _globals['_COLUMNEMBEDDINGPARAMETERS']._serialized_end=386
  _globals['_COLUMNEMBEDDINGPARAMETERS_COLUMNPARAMETERSENTRY']._serialized_start=286
  _globals['_COLUMNEMBEDDINGPARAMETERS_COLUMNPARAMETERSENTRY']._serialized_end=386
  _globals['_CONCATSTRINGANDEMBEDPARAMETERS']._serialized_start=389
  _globals['_CONCATSTRINGANDEMBEDPARAMETERS']._serialized_end=532
  _globals['_CONCATANDEMBEDPARAMETERS']._serialized_start=535
  _globals['_CONCATANDEMBEDPARAMETERS']._serialized_end=672
  _globals['_EMBEDANDCONCATPARAMETERS']._serialized_start=674
  _globals['_EMBEDANDCONCATPARAMETERS']._serialized_end=720
  _globals['_IMAGEMODELPARAMETERS']._serialized_start=722
  _globals['_IMAGEMODELPARAMETERS']._serialized_end=819
  _globals['_EMBEDIMAGEPARAMETERS']._serialized_start=822
  _globals['_EMBEDIMAGEPARAMETERS']._serialized_end=963
# @@protoc_insertion_point(module_scope)
