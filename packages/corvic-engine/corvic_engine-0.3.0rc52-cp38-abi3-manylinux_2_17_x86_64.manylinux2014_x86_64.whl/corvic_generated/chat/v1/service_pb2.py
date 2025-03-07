# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: corvic/chat/v1/service.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63orvic/chat/v1/service.proto\x12\x0e\x63orvic.chat.v1\x1a google/protobuf/descriptor.proto\"!\n\x0bUserMessage\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\"\xc7\x01\n\x0c\x41gentMessage\x12\x1f\n\x0b\x61gent_model\x18\x01 \x01(\tR\nagentModel\x12\x12\n\x04text\x18\x02 \x01(\tR\x04text\x12L\n\tdocuments\x18\x03 \x03(\x0b\x32..corvic.chat.v1.AgentMessage.DocumentReferenceR\tdocuments\x1a\x34\n\x11\x44ocumentReference\x12\x1f\n\x0b\x64ocument_id\x18\x01 \x01(\x03R\ndocumentId\"\xe8\x01\n\x0cMessageEntry\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tthread_id\x18\x02 \x01(\x03R\x08threadId\x12\x19\n\x08store_id\x18\x03 \x01(\x03R\x07storeId\x12@\n\x0cuser_message\x18\x04 \x01(\x0b\x32\x1b.corvic.chat.v1.UserMessageH\x00R\x0buserMessage\x12\x43\n\ragent_message\x18\x05 \x01(\x0b\x32\x1c.corvic.chat.v1.AgentMessageH\x00R\x0c\x61gentMessageB\t\n\x07\x63ontent\"8\n\x0bThreadEntry\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x19\n\x08store_id\x18\x02 \x01(\x03R\x07storeId\"0\n\x13\x43reateThreadRequest\x12\x19\n\x08store_id\x18\x02 \x01(\x03R\x07storeId\"I\n\x14\x43reateThreadResponse\x12\x31\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x1b.corvic.chat.v1.ThreadEntryR\x05\x65ntry\"%\n\x13\x44\x65leteThreadRequest\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\"\x16\n\x14\x44\x65leteThreadResponse\"/\n\x12ListThreadsRequest\x12\x19\n\x08store_id\x18\x01 \x01(\x03R\x07storeId\"H\n\x13ListThreadsResponse\x12\x31\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x1b.corvic.chat.v1.ThreadEntryR\x05\x65ntry\"G\n\x14\x41ppendMessageRequest\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1b\n\tthread_id\x18\x02 \x01(\x03R\x08threadId\"\x17\n\x15\x41ppendMessageResponse\"\x86\x01\n\x11GetMessagesCursor\x12\x1d\n\tthread_id\x18\x01 \x01(\x03H\x00R\x08threadId\x12\x1b\n\x08store_id\x18\x02 \x01(\x03H\x00R\x07storeId\x12*\n\x11last_message_sent\x18\x03 \x01(\x03R\x0flastMessageSentB\t\n\x07\x63ontent\"\x9d\x01\n\x12GetMessagesRequest\x12\x1d\n\tthread_id\x18\x01 \x01(\x03H\x00R\x08threadId\x12\x1b\n\x08store_id\x18\x02 \x01(\x03H\x00R\x07storeId\x12\x18\n\x06\x63ursor\x18\x03 \x01(\tH\x00R\x06\x63ursor\x12&\n\x0fmax_most_recent\x18\x04 \x01(\x04R\rmaxMostRecentB\t\n\x07\x63ontent\"*\n\x10UpToDateSentinel\x12\x16\n\x06\x63ursor\x18\x01 \x01(\tR\x06\x63ursor\"g\n\x13GetMessagesResponse\x12\x16\n\x06\x63ursor\x18\x01 \x01(\tR\x06\x63ursor\x12\x38\n\x08messages\x18\x02 \x03(\x0b\x32\x1c.corvic.chat.v1.MessageEntryR\x08messages2\xe7\x03\n\rThreadService\x12[\n\x0c\x43reateThread\x12#.corvic.chat.v1.CreateThreadRequest\x1a$.corvic.chat.v1.CreateThreadResponse\"\x00\x12[\n\x0c\x44\x65leteThread\x12#.corvic.chat.v1.DeleteThreadRequest\x1a$.corvic.chat.v1.DeleteThreadResponse\"\x00\x12]\n\x0bListThreads\x12\".corvic.chat.v1.ListThreadsRequest\x1a#.corvic.chat.v1.ListThreadsResponse\"\x03\x90\x02\x01\x30\x01\x12^\n\rAppendMessage\x12$.corvic.chat.v1.AppendMessageRequest\x1a%.corvic.chat.v1.AppendMessageResponse\"\x00\x12]\n\x0bGetMessages\x12\".corvic.chat.v1.GetMessagesRequest\x1a#.corvic.chat.v1.GetMessagesResponse\"\x03\x90\x02\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'corvic.chat.v1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_THREADSERVICE'].methods_by_name['ListThreads']._options = None
  _globals['_THREADSERVICE'].methods_by_name['ListThreads']._serialized_options = b'\220\002\001'
  _globals['_THREADSERVICE'].methods_by_name['GetMessages']._options = None
  _globals['_THREADSERVICE'].methods_by_name['GetMessages']._serialized_options = b'\220\002\001'
  _globals['_USERMESSAGE']._serialized_start=82
  _globals['_USERMESSAGE']._serialized_end=115
  _globals['_AGENTMESSAGE']._serialized_start=118
  _globals['_AGENTMESSAGE']._serialized_end=317
  _globals['_AGENTMESSAGE_DOCUMENTREFERENCE']._serialized_start=265
  _globals['_AGENTMESSAGE_DOCUMENTREFERENCE']._serialized_end=317
  _globals['_MESSAGEENTRY']._serialized_start=320
  _globals['_MESSAGEENTRY']._serialized_end=552
  _globals['_THREADENTRY']._serialized_start=554
  _globals['_THREADENTRY']._serialized_end=610
  _globals['_CREATETHREADREQUEST']._serialized_start=612
  _globals['_CREATETHREADREQUEST']._serialized_end=660
  _globals['_CREATETHREADRESPONSE']._serialized_start=662
  _globals['_CREATETHREADRESPONSE']._serialized_end=735
  _globals['_DELETETHREADREQUEST']._serialized_start=737
  _globals['_DELETETHREADREQUEST']._serialized_end=774
  _globals['_DELETETHREADRESPONSE']._serialized_start=776
  _globals['_DELETETHREADRESPONSE']._serialized_end=798
  _globals['_LISTTHREADSREQUEST']._serialized_start=800
  _globals['_LISTTHREADSREQUEST']._serialized_end=847
  _globals['_LISTTHREADSRESPONSE']._serialized_start=849
  _globals['_LISTTHREADSRESPONSE']._serialized_end=921
  _globals['_APPENDMESSAGEREQUEST']._serialized_start=923
  _globals['_APPENDMESSAGEREQUEST']._serialized_end=994
  _globals['_APPENDMESSAGERESPONSE']._serialized_start=996
  _globals['_APPENDMESSAGERESPONSE']._serialized_end=1019
  _globals['_GETMESSAGESCURSOR']._serialized_start=1022
  _globals['_GETMESSAGESCURSOR']._serialized_end=1156
  _globals['_GETMESSAGESREQUEST']._serialized_start=1159
  _globals['_GETMESSAGESREQUEST']._serialized_end=1316
  _globals['_UPTODATESENTINEL']._serialized_start=1318
  _globals['_UPTODATESENTINEL']._serialized_end=1360
  _globals['_GETMESSAGESRESPONSE']._serialized_start=1362
  _globals['_GETMESSAGESRESPONSE']._serialized_end=1465
  _globals['_THREADSERVICE']._serialized_start=1468
  _globals['_THREADSERVICE']._serialized_end=1955
# @@protoc_insertion_point(module_scope)
