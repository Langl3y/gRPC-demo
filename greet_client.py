import greet_pb2_grpc
import greet_pb2
import time
import grpc


def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting="Hello", name=name)
        yield hello_request
        time.sleep(1)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ServerSaysHello - Server Side Streaming")
        print("3. ClientSaysHello - Client Side Streaming")
        print("4. Interactive chat with server - Bi-directional streaming")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting="Hello", name="client")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)
        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting="Hello", name="Client")
            hello_replies = stub.ServerSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("ServerSaysHello Response Received:")
                print(hello_reply)
        elif rpc_call == "3":
            delayed_reply = stub.ClientSaysHello(get_client_stream_requests())

            print("ClientSaysHello Response Received:")
            print(delayed_reply)
        elif rpc_call == "4":
            responses = stub.ClientServerChat(get_client_stream_requests())

            for response in responses:
                print("Server Response Received: ")
                print(response)


if __name__ == "__main__":
    run()
