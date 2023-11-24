# gRPC-Python Demo 

## Requirements
* Python 3.10
* miniConda3 

Kích hoạt môi trường conda (cùng tên project):
```
conda activate grpctest
```

Upgrade pip: 
```
sudo -H pip3 install --upgrade pip
```

Cài đặt các package của gRPC protobuf cho python3:

```
pip install grpcio
pip install grpcio_tools
pip install protobuf 
```

Cấu trúc hiện tại của project:
```
grpctest/
├── protos/
│   └── greet.proto
├── greet_pb2.py
├── greet_pb2_grpc.py
├── greet_client.py
└── greet_server.py
```

Mở 2 terminal và chạy lần lượt 2 file dưới đây.

Chạy greet_server.py :
```
python3 greet_server.py
```

Chạy greet_client.py :
```
python3 greet_client.py
```

Terminal (greet_client.py):
```
1. SayHello - Unary
2. ServerSaysHello - Server Side Streaming
3. ClientSaysHello - Client Side Streaming
4. Interactive chat with server - Bi-directional streaming
Which rpc would you like to make: 
```

Chọn 1 trong 4 option trên để test demo các kiểu truyền data.
* Chọn 1 để test `unary streaming` - gửi và nhận data 1 lần duy nhất
* Chọn 2 hoặc 3 để test `server streaming` hoặc `client streaming` - gửi 1 request nhận nhiều responses dưới dạng tuần tự mà không đóng kết nối chỉ sau 1 response (khác với unary)
* Chọn 4 để test `bi-directional streaming` - client và server tuần tự gửi message cho nhau (đến khi client CTRL+C hoặc CTRL+Z)
