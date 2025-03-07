# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corvic/feature/v1/space.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from corvic_generated.ingest.v2 import source_pb2 as corvic_dot_ingest_dot_v2_dot_source__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63orvic/feature/v1/space.proto\x12\x11\x63orvic.feature.v1\x1a\x1b\x62uf/validate/validate.proto\x1a\x1d\x63orvic/ingest/v2/source.proto\x1a google/protobuf/descriptor.proto\"\xa1\x01\n\x0cOutputEntity\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12}\n\tsource_id\x18\x02 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x08sourceId\"\xb6\x01\n\x0bSpaceOutput\x12]\n\x16output_entity_operator\x18\x01 \x01(\x0e\x32\'.corvic.feature.v1.OutputEntityOperatorR\x14outputEntityOperator\x12H\n\x0foutput_entities\x18\x02 \x03(\x0b\x32\x1f.corvic.feature.v1.OutputEntityR\x0eoutputEntities\"\xdc\x03\n\nSpaceEntry\x12p\n\x02id\x18\x01 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x02id\x12\x19\n\x06org_id\x18\x02 \x01(\tB\x02\x18\x01R\x05orgId\x12y\n\x07room_id\x18\x03 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x06roomId\x12\x44\n\x0esource_entries\x18\x04 \x03(\x0b\x32\x1d.corvic.ingest.v2.SourceEntryR\rsourceEntries\x12\x1b\n\x04name\x18\x05 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x04name\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x41\n\x0cspace_output\x18\x07 \x01(\x0b\x32\x1e.corvic.feature.v1.SpaceOutputR\x0bspaceOutput\"\x83\x01\n\x0fGetSpaceRequest\x12p\n\x02id\x18\x01 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x02id\"R\n\x10GetSpaceResponse\x12>\n\x0bspace_entry\x18\x01 \x01(\x0b\x32\x1d.corvic.feature.v1.SpaceEntryR\nspaceEntry\"\x91\x01\n\x11ListSpacesRequest\x12|\n\x07room_id\x18\x01 \x01(\tBc\xbaH`\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')\xd0\x01\x01R\x06roomId\"X\n\x12ListSpacesResponse\x12\x42\n\rspace_entries\x18\x01 \x03(\x0b\x32\x1d.corvic.feature.v1.SpaceEntryR\x0cspaceEntries\"\x98\x03\n\x12\x43reateSpaceRequest\x12y\n\x07room_id\x18\x01 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x06roomId\x12\x1b\n\x04name\x18\x02 \x01(\tB\x07\xbaH\x04r\x02\x10\x01R\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x84\x01\n\nsource_ids\x18\x04 \x03(\tBe\xbaHb\x92\x01_\"]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\tsourceIds\x12\x41\n\x0cspace_output\x18\x05 \x01(\x0b\x32\x1e.corvic.feature.v1.SpaceOutputR\x0bspaceOutput\"U\n\x13\x43reateSpaceResponse\x12>\n\x0bspace_entry\x18\x01 \x01(\x0b\x32\x1d.corvic.feature.v1.SpaceEntryR\nspaceEntry\"\x86\x01\n\x12\x44\x65leteSpaceRequest\x12p\n\x02id\x18\x01 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x02id\"\x15\n\x13\x44\x65leteSpaceResponse\"\xe8\x01\n\x1cGetSpaceRelationshipsRequest\x12\x84\x01\n\nsource_ids\x18\x01 \x03(\tBe\xbaHb\x92\x01_\"]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\tsourceIds\x12\x41\n\x0cspace_output\x18\x02 \x01(\x0b\x32\x1e.corvic.feature.v1.SpaceOutputR\x0bspaceOutput\"\xba\x02\n\x12SourceRelationship\x12O\n\x12source_entry_start\x18\x01 \x01(\x0b\x32\x1d.corvic.ingest.v2.SourceEntryB\x02\x18\x01R\x10sourceEntryStart\x12K\n\x10source_entry_end\x18\x02 \x01(\x0b\x32\x1d.corvic.ingest.v2.SourceEntryB\x02\x18\x01R\x0esourceEntryEnd\x12&\n\x0fstart_source_id\x18\x03 \x01(\tR\rstartSourceId\x12\"\n\rend_source_id\x18\x04 \x01(\tR\x0b\x65ndSourceId\x12:\n\x19relationship_path_sources\x18\x05 \x03(\tR\x17relationshipPathSources\"y\n\x1dGetSpaceRelationshipsResponse\x12X\n\x14source_relationships\x18\x01 \x03(\x0b\x32%.corvic.feature.v1.SourceRelationshipR\x13sourceRelationships*\x8e\x01\n\x14OutputEntityOperator\x12&\n\"OUTPUT_ENTITY_OPERATOR_UNSPECIFIED\x10\x00\x12&\n\"OUTPUT_ENTITY_OPERATOR_CONJUNCTION\x10\x01\x12&\n\"OUTPUT_ENTITY_OPERATOR_DISJUNCTION\x10\x02\x32\x8e\x04\n\x0cSpaceService\x12X\n\x08GetSpace\x12\".corvic.feature.v1.GetSpaceRequest\x1a#.corvic.feature.v1.GetSpaceResponse\"\x03\x90\x02\x01\x12^\n\x0b\x43reateSpace\x12%.corvic.feature.v1.CreateSpaceRequest\x1a&.corvic.feature.v1.CreateSpaceResponse\"\x00\x12^\n\x0b\x44\x65leteSpace\x12%.corvic.feature.v1.DeleteSpaceRequest\x1a&.corvic.feature.v1.DeleteSpaceResponse\"\x00\x12^\n\nListSpaces\x12$.corvic.feature.v1.ListSpacesRequest\x1a%.corvic.feature.v1.ListSpacesResponse\"\x03\x90\x02\x01\x12\x7f\n\x15GetSpaceRelationships\x12/.corvic.feature.v1.GetSpaceRelationshipsRequest\x1a\x30.corvic.feature.v1.GetSpaceRelationshipsResponse\"\x03\x90\x02\x01\x1a\x03\x88\x02\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'corvic.feature.v1.space_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_OUTPUTENTITY'].fields_by_name['source_id']._options = None
  _globals['_OUTPUTENTITY'].fields_by_name['source_id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_SPACEENTRY'].fields_by_name['id']._options = None
  _globals['_SPACEENTRY'].fields_by_name['id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_SPACEENTRY'].fields_by_name['org_id']._options = None
  _globals['_SPACEENTRY'].fields_by_name['org_id']._serialized_options = b'\030\001'
  _globals['_SPACEENTRY'].fields_by_name['room_id']._options = None
  _globals['_SPACEENTRY'].fields_by_name['room_id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_SPACEENTRY'].fields_by_name['name']._options = None
  _globals['_SPACEENTRY'].fields_by_name['name']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_GETSPACEREQUEST'].fields_by_name['id']._options = None
  _globals['_GETSPACEREQUEST'].fields_by_name['id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_LISTSPACESREQUEST'].fields_by_name['room_id']._options = None
  _globals['_LISTSPACESREQUEST'].fields_by_name['room_id']._serialized_options = b'\272H`\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')\320\001\001'
  _globals['_CREATESPACEREQUEST'].fields_by_name['room_id']._options = None
  _globals['_CREATESPACEREQUEST'].fields_by_name['room_id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_CREATESPACEREQUEST'].fields_by_name['name']._options = None
  _globals['_CREATESPACEREQUEST'].fields_by_name['name']._serialized_options = b'\272H\004r\002\020\001'
  _globals['_CREATESPACEREQUEST'].fields_by_name['source_ids']._options = None
  _globals['_CREATESPACEREQUEST'].fields_by_name['source_ids']._serialized_options = b'\272Hb\222\001_\"]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_DELETESPACEREQUEST'].fields_by_name['id']._options = None
  _globals['_DELETESPACEREQUEST'].fields_by_name['id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_GETSPACERELATIONSHIPSREQUEST'].fields_by_name['source_ids']._options = None
  _globals['_GETSPACERELATIONSHIPSREQUEST'].fields_by_name['source_ids']._serialized_options = b'\272Hb\222\001_\"]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_SOURCERELATIONSHIP'].fields_by_name['source_entry_start']._options = None
  _globals['_SOURCERELATIONSHIP'].fields_by_name['source_entry_start']._serialized_options = b'\030\001'
  _globals['_SOURCERELATIONSHIP'].fields_by_name['source_entry_end']._options = None
  _globals['_SOURCERELATIONSHIP'].fields_by_name['source_entry_end']._serialized_options = b'\030\001'
  _globals['_SPACESERVICE']._options = None
  _globals['_SPACESERVICE']._serialized_options = b'\210\002\001'
  _globals['_SPACESERVICE'].methods_by_name['GetSpace']._options = None
  _globals['_SPACESERVICE'].methods_by_name['GetSpace']._serialized_options = b'\220\002\001'
  _globals['_SPACESERVICE'].methods_by_name['ListSpaces']._options = None
  _globals['_SPACESERVICE'].methods_by_name['ListSpaces']._serialized_options = b'\220\002\001'
  _globals['_SPACESERVICE'].methods_by_name['GetSpaceRelationships']._options = None
  _globals['_SPACESERVICE'].methods_by_name['GetSpaceRelationships']._serialized_options = b'\220\002\001'
  _globals['_OUTPUTENTITYOPERATOR']._serialized_start=2764
  _globals['_OUTPUTENTITYOPERATOR']._serialized_end=2906
  _globals['_OUTPUTENTITY']._serialized_start=147
  _globals['_OUTPUTENTITY']._serialized_end=308
  _globals['_SPACEOUTPUT']._serialized_start=311
  _globals['_SPACEOUTPUT']._serialized_end=493
  _globals['_SPACEENTRY']._serialized_start=496
  _globals['_SPACEENTRY']._serialized_end=972
  _globals['_GETSPACEREQUEST']._serialized_start=975
  _globals['_GETSPACEREQUEST']._serialized_end=1106
  _globals['_GETSPACERESPONSE']._serialized_start=1108
  _globals['_GETSPACERESPONSE']._serialized_end=1190
  _globals['_LISTSPACESREQUEST']._serialized_start=1193
  _globals['_LISTSPACESREQUEST']._serialized_end=1338
  _globals['_LISTSPACESRESPONSE']._serialized_start=1340
  _globals['_LISTSPACESRESPONSE']._serialized_end=1428
  _globals['_CREATESPACEREQUEST']._serialized_start=1431
  _globals['_CREATESPACEREQUEST']._serialized_end=1839
  _globals['_CREATESPACERESPONSE']._serialized_start=1841
  _globals['_CREATESPACERESPONSE']._serialized_end=1926
  _globals['_DELETESPACEREQUEST']._serialized_start=1929
  _globals['_DELETESPACEREQUEST']._serialized_end=2063
  _globals['_DELETESPACERESPONSE']._serialized_start=2065
  _globals['_DELETESPACERESPONSE']._serialized_end=2086
  _globals['_GETSPACERELATIONSHIPSREQUEST']._serialized_start=2089
  _globals['_GETSPACERELATIONSHIPSREQUEST']._serialized_end=2321
  _globals['_SOURCERELATIONSHIP']._serialized_start=2324
  _globals['_SOURCERELATIONSHIP']._serialized_end=2638
  _globals['_GETSPACERELATIONSHIPSRESPONSE']._serialized_start=2640
  _globals['_GETSPACERELATIONSHIPSRESPONSE']._serialized_end=2761
  _globals['_SPACESERVICE']._serialized_start=2909
  _globals['_SPACESERVICE']._serialized_end=3435
# @@protoc_insertion_point(module_scope)
