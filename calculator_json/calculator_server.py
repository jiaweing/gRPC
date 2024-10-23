import grpc
from concurrent import futures
import json

class CalculatorServicer:
    def Add(self, request, context):
        data = json.loads(request)
        result = data['x'] + data['y']
        return json.dumps({'result': result}).encode()

    def Sub(self, request, context):
        data = json.loads(request)
        result = data['x'] - data['y']
        return json.dumps({'result': result}).encode()

    def Multiply(self, request, context):
        data = json.loads(request)
        result = data['x'] * data['y']
        return json.dumps({'result': result}).encode()

    def Divide(self, request, context):
        data = json.loads(request)
        if data['y'] == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Division by zero')
            return json.dumps({'error': 'Division by zero'}).encode()
        result = data['x'] // data['y']
        return json.dumps({'result': result}).encode()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    rpc_method_handlers = {
        'Add': grpc.unary_unary_rpc_method_handler(
            CalculatorServicer().Add,
            request_deserializer=lambda x: x,
            response_serializer=lambda x: x,
        ),
        'Sub': grpc.unary_unary_rpc_method_handler(
            CalculatorServicer().Sub,
            request_deserializer=lambda x: x,
            response_serializer=lambda x: x,
        ),
        'Multiply': grpc.unary_unary_rpc_method_handler(
            CalculatorServicer().Multiply,
            request_deserializer=lambda x: x,
            response_serializer=lambda x: x,
        ),
        'Divide': grpc.unary_unary_rpc_method_handler(
            CalculatorServicer().Divide,
            request_deserializer=lambda x: x,
            response_serializer=lambda x: x,
        ),
    }
    
    generic_handler = grpc.method_handlers_generic_handler(
        'Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
