from rest_framework import serializers
from .models import UploadedFile

class RequestInfoSerializer(serializers.Serializer):
    method = serializers.CharField()
    get_data = serializers.DictField()
    post_data = serializers.DictField()
    user = serializers.CharField()
    is_logged_in = serializers.BooleanField()
    session_value = serializers.CharField()
    user_agent = serializers.CharField()
    client_ip = serializers.CharField()
    path = serializers.CharField()
    full_url = serializers.CharField()

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'title', 'file', 'uploaded_at']