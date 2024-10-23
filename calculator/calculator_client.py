import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    # Create a channel to the server
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client)
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        
        # Perform Add operation
        response = stub.Add(calculator_pb2.Request(x=10, y=5))
        print(f"Add: 10 + 5 = {response.res}")
        
        # Perform Sub operation
        response = stub.Sub(calculator_pb2.Request(x=10, y=5))
        print(f"Sub: 10 - 5 = {response.res}")
        
        # Perform Multiply operation
        response = stub.Multiply(calculator_pb2.Request(x=10, y=5))
        print(f"Multiply: 10 * 5 = {response.res}")
        
        # Perform Divide operation
        response = stub.Divide(calculator_pb2.Request(x=10, y=5))
        print(f"Divide: 10 / 5 = {response.res}")

if __name__ == '__main__':
    run()