from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def hello_api(request):
  return Response(
    {"message": "Hello"}
  )

@api_view(["POST"])
def receive_post(request):
  name = request.data.get('name')
  message = request.data.get('message')

  if not name or not message:
    return Response(
      {"message": "Please enter your name and message"},
      status=status.HTTP_400_BAD_REQUEST
    )

  return Response(
    {"message": f"{name} sent a message: {message}"},
    status=status.HTTP_200_OK
  )
