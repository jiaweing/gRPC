import grpc
import json

class CalculatorStub:
    def __init__(self, channel):
        self.channel = channel

    def Add(self, x, y):
        request = json.dumps({'x': x, 'y': y})
        response = self.channel.unary_unary('/Calculator/Add')(request.encode())
        return json.loads(response)

    def Sub(self, x, y):
        request = json.dumps({'x': x, 'y': y})
        response = self.channel.unary_unary('/Calculator/Sub')(request.encode())
        return json.loads(response)

    def Multiply(self, x, y):
        request = json.dumps({'x': x, 'y': y})
        response = self.channel.unary_unary('/Calculator/Multiply')(request.encode())
        return json.loads(response)

    def Divide(self, x, y):
        request = json.dumps({'x': x, 'y': y})
        response = self.channel.unary_unary('/Calculator/Divide')(request.encode())
        return json.loads(response)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CalculatorStub(channel)
        
        # Perform Add operation
        result = stub.Add(10, 5)
        print(f"Add: 10 + 5 = {result['result']}")
        
        # Perform Sub operation
        result = stub.Sub(10, 5)
        print(f"Sub: 10 - 5 = {result['result']}")
        
        # Perform Multiply operation
        result = stub.Multiply(10, 5)
        print(f"Multiply: 10 * 5 = {result['result']}")
        
        # Perform Divide operation
        result = stub.Divide(10, 5)
        print(f"Divide: 10 / 5 = {result['result']}")

if __name__ == '__main__':
    run()
