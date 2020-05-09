# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import file_server_pb2 as file__server__pb2


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upload = channel.stream_unary(
                '/FileService/Upload',
                request_serializer=file__server__pb2.Chunk.SerializeToString,
                response_deserializer=file__server__pb2.UploadStatus.FromString,
                )


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upload': grpc.stream_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=file__server__pb2.Chunk.FromString,
                    response_serializer=file__server__pb2.UploadStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/FileService/Upload',
            file__server__pb2.Chunk.SerializeToString,
            file__server__pb2.UploadStatus.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
