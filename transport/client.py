import grpc
import json
import transport_pb2
import transport_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = transport_pb2_grpc.PublicTransportStub(channel)

        # Example 1: Get Bus Arrival Time
        bus_arrival_request = transport_pb2.BusArrivalRequest(bus_stop_code="65009", service_no="84W")
        response = stub.GetBusArrival(bus_arrival_request)
        print(f"Bus {response.service_no} arrives at {response.next_arrival_time} with {response.load}. The next bus will be at {response.next_arrival_time2}")

        # Example 2: Get Bus Service Info
        bus_service_request = transport_pb2.BusServiceRequest(bus_service_code="50")
        response = stub.GetBusServiceInfo(bus_service_request)
        print(f"Bus Service: 50, Operated by: {response.operator}, Origin: {response.origin_name}, Destination: {response.destination_name}.")
        if (response.loop == 'YES'):
            print(f"Ths bus is a loop service.")
        else:
            print(f"Ths bus is not a loop service.")

if __name__ == "__main__":
    run()
