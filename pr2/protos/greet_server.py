from concurrent import futures
import time
import grpc
import greet_pb2
import greet_pb2_grpc

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("SayHello Request Made:")
        # print(request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.message}"

        print(hello_reply)

    def ParrotSaysHello(self, request, context):
        print("ParrotSaysHello request made")
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting}{request.message}"
        print(hello_reply)

    def ChattyClientSaysHello(self, request, context):
        print("ChattyClientSayHello request made")
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.message}"

    def InteractingHello(self, request, context):
        print("InteractingHello request made")
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.message}"
        print(hello_reply)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    print("Starting server")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()