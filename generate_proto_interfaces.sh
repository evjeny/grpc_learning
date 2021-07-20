python -m grpc_tools.protoc --proto_path=protos/ \
    --python_out=interfaces/ \
    --grpc_python_out=interfaces/ \
    protos/capitalizer.proto