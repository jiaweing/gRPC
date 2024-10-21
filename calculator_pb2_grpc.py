# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import calculator_pb2 as calculator__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in calculator_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CalculatorStub(object):
    """The calculator service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/calculator.Calculator/Add',
                request_serializer=calculator__pb2.Request.SerializeToString,
                response_deserializer=calculator__pb2.Reply.FromString,
                _registered_method=True)
        self.Sub = channel.unary_unary(
                '/calculator.Calculator/Sub',
                request_serializer=calculator__pb2.Request.SerializeToString,
                response_deserializer=calculator__pb2.Reply.FromString,
                _registered_method=True)
        self.Multiply = channel.unary_unary(
                '/calculator.Calculator/Multiply',
                request_serializer=calculator__pb2.Request.SerializeToString,
                response_deserializer=calculator__pb2.Reply.FromString,
                _registered_method=True)
        self.Divide = channel.unary_unary(
                '/calculator.Calculator/Divide',
                request_serializer=calculator__pb2.Request.SerializeToString,
                response_deserializer=calculator__pb2.Reply.FromString,
                _registered_method=True)


class CalculatorServicer(object):
    """The calculator service definition.
    """

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sub(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Multiply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Divide(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=calculator__pb2.Request.FromString,
                    response_serializer=calculator__pb2.Reply.SerializeToString,
            ),
            'Sub': grpc.unary_unary_rpc_method_handler(
                    servicer.Sub,
                    request_deserializer=calculator__pb2.Request.FromString,
                    response_serializer=calculator__pb2.Reply.SerializeToString,
            ),
            'Multiply': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiply,
                    request_deserializer=calculator__pb2.Request.FromString,
                    response_serializer=calculator__pb2.Reply.SerializeToString,
            ),
            'Divide': grpc.unary_unary_rpc_method_handler(
                    servicer.Divide,
                    request_deserializer=calculator__pb2.Request.FromString,
                    response_serializer=calculator__pb2.Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calculator.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('calculator.Calculator', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """The calculator service definition.
    """

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/calculator.Calculator/Add',
            calculator__pb2.Request.SerializeToString,
            calculator__pb2.Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Sub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/calculator.Calculator/Sub',
            calculator__pb2.Request.SerializeToString,
            calculator__pb2.Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Multiply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/calculator.Calculator/Multiply',
            calculator__pb2.Request.SerializeToString,
            calculator__pb2.Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Divide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/calculator.Calculator/Divide',
            calculator__pb2.Request.SerializeToString,
            calculator__pb2.Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
