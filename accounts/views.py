from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
import logging

logger = logging.getLogger('accounts')

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        logger.info("LoginAPIView called")
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            logger.info(f"LoginAPIView response: {user.username}")
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        logger.warning("LoginAPIView response: Invalid username or password")
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class HomeAPIView(APIView):
    logger.info("HomeAPIView called")
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logger.info(f"HomeAPIView response: {request.user.username}")
        return Response({'message': f'Welcome {request.user.username}!'}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    logger.info("LogoutAPIView called")
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        logger.info("LogoutAPIView response: Logged out successfully")
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)