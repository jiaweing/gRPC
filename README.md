# Generate protobuf

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

# Run Server

```
python calculator_server.py
```

# Run Client

```
python calculator_client.py
```
