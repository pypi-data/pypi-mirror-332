# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corvic/orm/v1/space.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from corvic_generated.algorithm.graph.v1 import graph_pb2 as corvic_dot_algorithm_dot_graph_dot_v1_dot_graph__pb2
from corvic_generated.embedding.v1 import models_pb2 as corvic_dot_embedding_dot_v1_dot_models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63orvic/orm/v1/space.proto\x12\rcorvic.orm.v1\x1a%corvic/algorithm/graph/v1/graph.proto\x1a corvic/embedding/v1/models.proto\"\xc9\x04\n\x0fSpaceParameters\x12p\n\x1b\x63olumn_embedding_parameters\x18\x02 \x01(\x0b\x32..corvic.embedding.v1.ColumnEmbeddingParametersH\x00R\x19\x63olumnEmbeddingParameters\x12`\n\x13node2vec_parameters\x18\x03 \x01(\x0b\x32-.corvic.algorithm.graph.v1.Node2VecParametersH\x00R\x12node2vecParameters\x12n\n\x1b\x63oncat_and_embed_parameters\x18\x04 \x01(\x0b\x32-.corvic.embedding.v1.ConcatAndEmbedParametersH\x00R\x18\x63oncatAndEmbedParameters\x12n\n\x1b\x65mbed_and_concat_parameters\x18\x05 \x01(\x0b\x32-.corvic.embedding.v1.EmbedAndConcatParametersH\x00R\x18\x65mbedAndConcatParameters\x12\x61\n\x16\x65mbed_image_parameters\x18\x06 \x01(\x0b\x32).corvic.embedding.v1.EmbedImageParametersH\x00R\x14\x65mbedImageParametersB\x08\n\x06paramsJ\x04\x08\x01\x10\x02R\x0f\x66\x65\x61ture_view_idb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'corvic.orm.v1.space_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SPACEPARAMETERS']._serialized_start=118
  _globals['_SPACEPARAMETERS']._serialized_end=703
# @@protoc_insertion_point(module_scope)
