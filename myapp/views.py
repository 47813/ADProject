from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger('myapp')

@api_view(["GET"])
def hello_api(request):
  logger.info("hello_api called")
  return Response(
    {"message": "Hello"}
  )

@api_view(["POST"])
def receive_post(request):
  logger.info("receive_post called")
  name = request.data.get('name')
  message = request.data.get('message')

  if not name or not message:
    logger.warning("receive_post response: Please enter your name and message")
    return Response(
      {"message": "Please enter your name and message"},
      status=status.HTTP_400_BAD_REQUEST
    )

  logger.info(f"receive_post response: {name} sent a message: {message}")
  return Response(
    {"message": f"{name} sent a message: {message}"},
    status=status.HTTP_200_OK
  )
