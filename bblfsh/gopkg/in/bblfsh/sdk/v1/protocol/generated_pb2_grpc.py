# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import generated_pb2 as generated__pb2


class ProtocolServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NativeParse = channel.unary_unary(
        '/gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService/NativeParse',
        request_serializer=generated__pb2.NativeParseRequest.SerializeToString,
        response_deserializer=generated__pb2.NativeParseResponse.FromString,
        )
    self.Parse = channel.unary_unary(
        '/gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService/Parse',
        request_serializer=generated__pb2.ParseRequest.SerializeToString,
        response_deserializer=generated__pb2.ParseResponse.FromString,
        )
    self.Version = channel.unary_unary(
        '/gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService/Version',
        request_serializer=generated__pb2.VersionRequest.SerializeToString,
        response_deserializer=generated__pb2.VersionResponse.FromString,
        )


class ProtocolServiceServicer(object):

  def NativeParse(self, request, context):
    """NativeParse uses DefaultService to process the given parsing request to get
    the AST.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Parse(self, request, context):
    """Parse uses DefaultService to process the given parsing request to get the UAST.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Version(self, request, context):
    """Version uses DefaultVersioner to process the given version request to get the version.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProtocolServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NativeParse': grpc.unary_unary_rpc_method_handler(
          servicer.NativeParse,
          request_deserializer=generated__pb2.NativeParseRequest.FromString,
          response_serializer=generated__pb2.NativeParseResponse.SerializeToString,
      ),
      'Parse': grpc.unary_unary_rpc_method_handler(
          servicer.Parse,
          request_deserializer=generated__pb2.ParseRequest.FromString,
          response_serializer=generated__pb2.ParseResponse.SerializeToString,
      ),
      'Version': grpc.unary_unary_rpc_method_handler(
          servicer.Version,
          request_deserializer=generated__pb2.VersionRequest.FromString,
          response_serializer=generated__pb2.VersionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gopkg.in.bblfsh.sdk.v1.protocol.ProtocolService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
