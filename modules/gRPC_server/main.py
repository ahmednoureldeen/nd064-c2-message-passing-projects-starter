import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from services import save_location


class LocationServicer(location_pb2_grpc.LocationServiceServicer):

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude,
        }
        print(request_value)
        save_location(request_value)
        return location_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)