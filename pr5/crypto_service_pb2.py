# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63rypto_service.proto\",\n\x0e\x63ryptocurrency\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\x80\x01\n\x0cmarket_price\x12\x16\n\tmax_price\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x16\n\tmin_price\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x16\n\tavg_price\x18\x03 \x01(\x02H\x02\x88\x01\x01\x42\x0c\n\n_max_priceB\x0c\n\n_min_priceB\x0c\n\n_avg_price2:\n\tGExchange\x12-\n\tget_price\x12\x0f.cryptocurrency\x1a\r.market_price\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crypto_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CRYPTOCURRENCY._serialized_start=24
  _CRYPTOCURRENCY._serialized_end=68
  _MARKET_PRICE._serialized_start=71
  _MARKET_PRICE._serialized_end=199
  _GEXCHANGE._serialized_start=201
  _GEXCHANGE._serialized_end=259
# @@protoc_insertion_point(module_scope)
