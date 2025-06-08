from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import UploadedFileSerializer, RequestInfoSerializer

class RequestInfoAPIView(APIView):
    def get(self, request, format=None):
        data = {
            'method': request.method,
            'get_data': request.GET,
            'post_data': request.POST,
            'user': str(request.user),
            'is_logged_in': request.user.is_authenticated,
            'session_value': request.session.get('demo', '없음'),
            'user_agent': request.META.get('HTTP_USER_AGENT', '알 수 없음'),
            'client_ip': request.META.get('REMOTE_ADDR', '알 수 없음'),
            'path': request.path,
            'full_url': request.build_absolute_uri()
        }

        request.session['demo'] = '세션에서 저장한 값입니다.'
        serializer = RequestInfoSerializer(data)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = {
            'method': request.method,
            'get_data': request.GET,
            'post_data': request.POST,
            'user': str(request.user),
            'is_logged_in': request.user.is_authenticated,
            'session_value': request.session.get('demo', '없음'),
            'user_agent': request.META.get('HTTP_USER_AGENT', '알 수 없음'),
            'client_ip': request.META.get('REMOTE_ADDR', '알 수 없음'),
            'path': request.path,
            'full_url': request.build_absolute_uri()
        }

        request.session['demo'] = '세션에서 저장한 값입니다.'
        serializer = RequestInfoSerializer(data)
        return Response(serializer.data)


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)