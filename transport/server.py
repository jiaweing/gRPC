import grpc
from concurrent import futures
import time
import json
#TODO:import _pb2 and _pb2_grpc files
import transport_pb2
import transport_pb2_grpc

class PublicTransportServicer(transport_pb2_grpc.PublicTransportServicer):

    # Implement GetBusArrival RPC
    def GetBusArrival(self, request, context):
        #read from LTA Data -- data/BusArrival.JSON
        with open('data/BusArrival.json', 'r') as file:
            bus_data = json.load(file)

        #TODO:obtain the data from bus_data to be returned to the client #####
        bus_stop_code = request.bus_stop_code
        service_no = request.service_no
        bus_stops = bus_data['busStops']
        
        for x in bus_stops:
            if x['BusStopCode'] == bus_stop_code:
                bus_services = x['Services']
                for y in bus_services:
                    if y['ServiceNo'] == service_no:
                        #TODO:return a response to client
                        return transport_pb2.BusArrivalResponse(service_no=y['ServiceNo'],
                            next_arrival_time=y['NextBus']['EstimatedArrival'],
                            next_arrival_time2=y['NextBus2']['EstimatedArrival'],
                            load=y['NextBus']['Load'],
                            bus_type=y['NextBus']['Type'])

        # return default if not found
        return transport_pb2.BusArrivalResponse()
    
    # Implement GetBusServiceInfo RPC
    def GetBusServiceInfo(self, request, context):

        #read from LTA Data -- data/BusServices.JSON
        with open('data/BusServices.json', 'r') as file:
            bus_info = json.load(file)

        #TODO:obtain the data from bus_info to be returned to the client #####
        bus_service_code = request.bus_service_code
        bus_services = bus_info['value']
        
        for x in bus_services:
            if x['ServiceNo'] == bus_service_code:
                        #TODO:return a response to client
                        return transport_pb2.BusServiceResponse(bus_service_no=x['ServiceNo'],
                            origin_name=x['Origin'],
                            destination_name=x['Destination'],
                            loop=x['Loop'],
                            operator=x['Operator'])
        
        # return default if not found
        return transport_pb2.BusServiceResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #TODO: bind the Servicer to Server #####
    transport_pb2_grpc.add_PublicTransportServicer_to_server(PublicTransportServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
