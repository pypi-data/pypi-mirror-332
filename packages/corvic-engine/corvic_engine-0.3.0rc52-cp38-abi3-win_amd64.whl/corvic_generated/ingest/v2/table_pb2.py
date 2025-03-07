# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corvic/ingest/v2/table.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2
from corvic_generated.orm.v1 import table_pb2 as corvic_dot_orm_dot_v1_dot_table__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63orvic/ingest/v2/table.proto\x12\x10\x63orvic.ingest.v2\x1a\x1b\x62uf/validate/validate.proto\x1a\x19\x63orvic/orm/v1/table.proto\x1a google/protobuf/descriptor.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xe3\x01\n\x0c\x43olumnSchema\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05\x64type\x18\x02 \x01(\tR\x05\x64type\x12\x18\n\x05\x66type\x18\x03 \x01(\tB\x02\x18\x01R\x05\x66type\x12=\n\x0c\x66\x65\x61ture_type\x18\x04 \x01(\x0b\x32\x1a.corvic.orm.v1.FeatureTypeR\x0b\x66\x65\x61tureType\x12P\n\x16possible_feature_types\x18\x05 \x03(\x0b\x32\x1a.corvic.orm.v1.FeatureTypeR\x14possibleFeatureTypes\"G\n\x0bTableSchema\x12\x38\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x1e.corvic.ingest.v2.ColumnSchemaR\x07\x63olumns\"\xa3\x01\n\nTableEntry\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x19\n\x08num_rows\x18\x04 \x01(\x03R\x07numRows\x12\x35\n\x06schema\x18\x05 \x01(\x0b\x32\x1d.corvic.ingest.v2.TableSchemaR\x06schema\"8\n\tTableData\x12+\n\x04rows\x18\x01 \x03(\x0b\x32\x17.google.protobuf.StructR\x04rows\"\x86\x01\n\x12\x44\x65leteTableRequest\x12p\n\x02id\x18\x01 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x02id\"\x15\n\x13\x44\x65leteTableResponse\"\x83\x01\n\x0fGetTableRequest\x12p\n\x02id\x18\x01 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x02id\"F\n\x10GetTableResponse\x12\x32\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x1c.corvic.ingest.v2.TableEntryR\x05\x65ntry\"\x98\x02\n\x11ListTablesRequest\x12|\n\x07room_id\x18\x01 \x01(\tBc\xbaH`\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')\xd0\x01\x01R\x06roomId\x12\x84\x01\n\x0bresource_id\x18\x02 \x01(\tBc\xbaH`\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')\xd0\x01\x01R\nresourceId\"H\n\x12ListTablesResponse\x12\x32\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x1c.corvic.ingest.v2.TableEntryR\x05\x65ntry\"\x87\x01\n\x13GetTableHeadRequest\x12p\n\x02id\x18\x01 \x01(\tB`\xbaH]\xba\x01Z\n\x0estring.pattern\x12\x16value must be a number\x1a\x30this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')R\x02id\"{\n\x14GetTableHeadResponse\x12\x32\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x1c.corvic.ingest.v2.TableEntryR\x05\x65ntry\x12/\n\x04head\x18\x02 \x01(\x0b\x32\x1b.corvic.ingest.v2.TableDataR\x04head2\x8d\x03\n\x0cTableService\x12\\\n\x0b\x44\x65leteTable\x12$.corvic.ingest.v2.DeleteTableRequest\x1a%.corvic.ingest.v2.DeleteTableResponse\"\x00\x12V\n\x08GetTable\x12!.corvic.ingest.v2.GetTableRequest\x1a\".corvic.ingest.v2.GetTableResponse\"\x03\x90\x02\x01\x12^\n\nListTables\x12#.corvic.ingest.v2.ListTablesRequest\x1a$.corvic.ingest.v2.ListTablesResponse\"\x03\x90\x02\x01\x30\x01\x12\x62\n\x0cGetTableHead\x12%.corvic.ingest.v2.GetTableHeadRequest\x1a&.corvic.ingest.v2.GetTableHeadResponse\"\x03\x90\x02\x01\x1a\x03\x88\x02\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'corvic.ingest.v2.table_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COLUMNSCHEMA'].fields_by_name['ftype']._options = None
  _globals['_COLUMNSCHEMA'].fields_by_name['ftype']._serialized_options = b'\030\001'
  _globals['_DELETETABLEREQUEST'].fields_by_name['id']._options = None
  _globals['_DELETETABLEREQUEST'].fields_by_name['id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_GETTABLEREQUEST'].fields_by_name['id']._options = None
  _globals['_GETTABLEREQUEST'].fields_by_name['id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_LISTTABLESREQUEST'].fields_by_name['room_id']._options = None
  _globals['_LISTTABLESREQUEST'].fields_by_name['room_id']._serialized_options = b'\272H`\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')\320\001\001'
  _globals['_LISTTABLESREQUEST'].fields_by_name['resource_id']._options = None
  _globals['_LISTTABLESREQUEST'].fields_by_name['resource_id']._serialized_options = b'\272H`\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')\320\001\001'
  _globals['_GETTABLEHEADREQUEST'].fields_by_name['id']._options = None
  _globals['_GETTABLEHEADREQUEST'].fields_by_name['id']._serialized_options = b'\272H]\272\001Z\n\016string.pattern\022\026value must be a number\0320this.matches(\'^[0-9]+$\') && !this.endsWith(\'\\n\')'
  _globals['_TABLESERVICE']._options = None
  _globals['_TABLESERVICE']._serialized_options = b'\210\002\001'
  _globals['_TABLESERVICE'].methods_by_name['GetTable']._options = None
  _globals['_TABLESERVICE'].methods_by_name['GetTable']._serialized_options = b'\220\002\001'
  _globals['_TABLESERVICE'].methods_by_name['ListTables']._options = None
  _globals['_TABLESERVICE'].methods_by_name['ListTables']._serialized_options = b'\220\002\001'
  _globals['_TABLESERVICE'].methods_by_name['GetTableHead']._options = None
  _globals['_TABLESERVICE'].methods_by_name['GetTableHead']._serialized_options = b'\220\002\001'
  _globals['_COLUMNSCHEMA']._serialized_start=171
  _globals['_COLUMNSCHEMA']._serialized_end=398
  _globals['_TABLESCHEMA']._serialized_start=400
  _globals['_TABLESCHEMA']._serialized_end=471
  _globals['_TABLEENTRY']._serialized_start=474
  _globals['_TABLEENTRY']._serialized_end=637
  _globals['_TABLEDATA']._serialized_start=639
  _globals['_TABLEDATA']._serialized_end=695
  _globals['_DELETETABLEREQUEST']._serialized_start=698
  _globals['_DELETETABLEREQUEST']._serialized_end=832
  _globals['_DELETETABLERESPONSE']._serialized_start=834
  _globals['_DELETETABLERESPONSE']._serialized_end=855
  _globals['_GETTABLEREQUEST']._serialized_start=858
  _globals['_GETTABLEREQUEST']._serialized_end=989
  _globals['_GETTABLERESPONSE']._serialized_start=991
  _globals['_GETTABLERESPONSE']._serialized_end=1061
  _globals['_LISTTABLESREQUEST']._serialized_start=1064
  _globals['_LISTTABLESREQUEST']._serialized_end=1344
  _globals['_LISTTABLESRESPONSE']._serialized_start=1346
  _globals['_LISTTABLESRESPONSE']._serialized_end=1418
  _globals['_GETTABLEHEADREQUEST']._serialized_start=1421
  _globals['_GETTABLEHEADREQUEST']._serialized_end=1556
  _globals['_GETTABLEHEADRESPONSE']._serialized_start=1558
  _globals['_GETTABLEHEADRESPONSE']._serialized_end=1681
  _globals['_TABLESERVICE']._serialized_start=1684
  _globals['_TABLESERVICE']._serialized_end=2081
# @@protoc_insertion_point(module_scope)
