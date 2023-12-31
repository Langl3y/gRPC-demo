# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greet_pb2 as greet__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/greet.Greeter/SayHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )
        self.ServerSaysHello = channel.unary_stream(
                '/greet.Greeter/ServerSaysHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )
        self.ClientSaysHello = channel.stream_unary(
                '/greet.Greeter/ClientSaysHello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.DelayedReply.FromString,
                )
        self.ClientServerChat = channel.stream_stream(
                '/greet.Greeter/ClientServerChat',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Unary streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServerSaysHello(self, request, context):
        """Server Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientSaysHello(self, request_iterator, context):
        """Client Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClientServerChat(self, request_iterator, context):
        """Bi-directional streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
            'ServerSaysHello': grpc.unary_stream_rpc_method_handler(
                    servicer.ServerSaysHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
            'ClientSaysHello': grpc.stream_unary_rpc_method_handler(
                    servicer.ClientSaysHello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.DelayedReply.SerializeToString,
            ),
            'ClientServerChat': grpc.stream_stream_rpc_method_handler(
                    servicer.ClientServerChat,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greet.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greet.Greeter/SayHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServerSaysHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greet.Greeter/ServerSaysHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientSaysHello(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/greet.Greeter/ClientSaysHello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.DelayedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClientServerChat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/greet.Greeter/ClientServerChat',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
