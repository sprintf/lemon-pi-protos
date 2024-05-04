# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import lemon_pi_pb2 as lemon__pi__pb2


class CommsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PingPong = channel.unary_unary(
                '/CommsService/PingPong',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.sendMessageFromCar = channel.unary_unary(
                '/CommsService/sendMessageFromCar',
                request_serializer=lemon__pi__pb2.ToPitMessage.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.sendMessageFromPits = channel.unary_unary(
                '/CommsService/sendMessageFromPits',
                request_serializer=lemon__pi__pb2.ToCarMessage.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.receivePitMessages = channel.unary_stream(
                '/CommsService/receivePitMessages',
                request_serializer=lemon__pi__pb2.CarNumber.SerializeToString,
                response_deserializer=lemon__pi__pb2.ToCarMessage.FromString,
                )
        self.receiveCarMessages = channel.unary_stream(
                '/CommsService/receiveCarMessages',
                request_serializer=lemon__pi__pb2.CarNumber.SerializeToString,
                response_deserializer=lemon__pi__pb2.ToPitMessage.FromString,
                )


class CommsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PingPong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendMessageFromCar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendMessageFromPits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def receivePitMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def receiveCarMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PingPong': grpc.unary_unary_rpc_method_handler(
                    servicer.PingPong,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'sendMessageFromCar': grpc.unary_unary_rpc_method_handler(
                    servicer.sendMessageFromCar,
                    request_deserializer=lemon__pi__pb2.ToPitMessage.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'sendMessageFromPits': grpc.unary_unary_rpc_method_handler(
                    servicer.sendMessageFromPits,
                    request_deserializer=lemon__pi__pb2.ToCarMessage.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'receivePitMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.receivePitMessages,
                    request_deserializer=lemon__pi__pb2.CarNumber.FromString,
                    response_serializer=lemon__pi__pb2.ToCarMessage.SerializeToString,
            ),
            'receiveCarMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.receiveCarMessages,
                    request_deserializer=lemon__pi__pb2.CarNumber.FromString,
                    response_serializer=lemon__pi__pb2.ToPitMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CommsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CommsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PingPong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommsService/PingPong',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendMessageFromCar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommsService/sendMessageFromCar',
            lemon__pi__pb2.ToPitMessage.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendMessageFromPits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CommsService/sendMessageFromPits',
            lemon__pi__pb2.ToCarMessage.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def receivePitMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/CommsService/receivePitMessages',
            lemon__pi__pb2.CarNumber.SerializeToString,
            lemon__pi__pb2.ToCarMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def receiveCarMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/CommsService/receiveCarMessages',
            lemon__pi__pb2.CarNumber.SerializeToString,
            lemon__pi__pb2.ToPitMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
