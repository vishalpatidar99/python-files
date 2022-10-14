import greet_pb2_grpc
import greet_pb2
import grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server side Streaming")
        print("3. ChattyclientSaysHelo - client side streaming")
        print("4. InteractingHello -Both Streaming")
        rpc_call = input("which rpc would you like to make: ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting = "Hello everyone, ",message="vishal")
            hello_reply = stub.SayHello(hello_request)
            # print(("Hello response recieved"))
            # print(hello_reply)
            # return hello_reply

        elif rpc_call == "2":
            #print("Not")
            hello_request = greet_pb2.HelloRequest(greeting = "Hello parrot")
            hello_reply = stub.ParrotSaysHello(hello_request)
            print("Streaming")

        elif rpc_call == "3":
            hello_request = greet_pb2.HelloRequest(greeting = "hello Chatty", message="sknllsd")
            hello_reply = stub.ChattyClientSaysHello(hello_request)
            print("Done")

        elif rpc_call == "4":
            hello_request = greet_pb2.HelloRequest(greeting = "Hello this is streaming, it's me ", message="Vishal")
            hello_reply = stub.InteractingHello(hello_request)
            # return hello_reply
            print("intracting")

if __name__ == "__main__":
    run()