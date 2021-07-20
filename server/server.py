from interfaces import capitalizer_pb2, capitalizer_pb2_grpc


class Capitalizer(capitalizer_pb2_grpc.CapitalizerServicer):

    def Capitalize(self, request, context):
        return capitalizer_pb2.StringResponse(message=request.message.capitalize())

    def Upper(self, request, context):
        return capitalizer_pb2.StringResponse(message=request.message.upper())
    
    def Lower(self, request, context):
        return capitalizer_pb2.StringResponse(message=request.message.lower())