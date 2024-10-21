import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return calculator_pb2.Reply(res=request.x + request.y)

    def Sub(self, request, context):
        return calculator_pb2.Reply(res=request.x - request.y)

    def Multiply(self, request, context):
        return calculator_pb2.Reply(res=request.x * request.y)

    def Divide(self, request, context):
        if request.y == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Division by zero')
            return calculator_pb2.Reply()
        return calculator_pb2.Reply(res=request.x // request.y)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()