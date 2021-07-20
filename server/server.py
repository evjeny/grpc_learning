import io
from PIL import Image, ImageDraw

from interfaces import capitalizer_pb2, capitalizer_pb2_grpc


class Capitalizer(capitalizer_pb2_grpc.CapitalizerServicer):

    def Capitalize(self, request, context):
        return capitalizer_pb2.StringResponse(message=request.message.capitalize())

    def Upper(self, request, context):
        return capitalizer_pb2.StringResponse(message=request.message.upper())
    
    def Lower(self, request, context):
        return capitalizer_pb2.StringResponse(message=request.message.lower())
    
    def DrawA(self, request, context):
        buffer = io.BytesIO(request.file)
        image = Image.open(buffer)
        width, height = image.size
        
        draw = ImageDraw.Draw(image)
        draw.line([(0, height), (width // 2, 0), (width, height)], width=4, fill="red")

        buffer = io.BytesIO()
        image.save(buffer, "png")

        return capitalizer_pb2.FileResponse(file=buffer.getvalue())
    
    def UpperPoints(self, request, context):
        result = [
            capitalizer_pb2.Point(x=p.x, y=p.y, value=p.value.upper())
            for p in request.points
        ]
        return capitalizer_pb2.PointsResponse(points=result)
    
    def DoAction(self, request, context):
        action = request.action
        if action == capitalizer_pb2.Action.NOTHING:
            message = request.message
        elif action == capitalizer_pb2.Action.CAPITALIZE:
            message = request.message.capitalize()
        elif action == capitalizer_pb2.Action.UPPER:
            message = request.message.upper()
        elif action == capitalizer_pb2.Action.LOWER:
            message = request.message.lower()
        else:
            message = "!!!"
        
        return capitalizer_pb2.StringResponse(message=message)
    
    def OptionalUpper(self, request, context):
        return capitalizer_pb2.StringResponse(message=request.message.upper())
