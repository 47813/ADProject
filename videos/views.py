from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
import logging

logger = logging.getLogger('videos')

@api_view(['GET'])
def get_all_videos_view(request):
    logger.info("get_all_videos_view called")
    videos = Video.get_all_videos()
    serializer = VideoSerializer(videos, many=True)
    logger.info(f"get_all_videos_view response: {serializer.data}")
    return Response({'videos': serializer.data})

@api_view(['GET'])
def get_videos_by_author_view(request, author_name):
    logger.info(f"get_videos_by_author_view called with author_name: {author_name}")
    videos = Video.objects.filter(author__icontains=author_name)
    serializer = VideoSerializer(videos, many=True)
    logger.info(f"get_videos_by_author_view response: {serializer.data}")
    return Response({'videos': serializer.data})

@api_view(['GET'])
def get_videos_by_title_keyword_view(request, keyword):
    logger.info(f"get_videos_by_title_keyword_view called with keyword: {keyword}")
    videos = Video.objects.filter(title__icontains=keyword)
    serializer = VideoSerializer(videos, many=True)
    logger.info(f"get_videos_by_title_keyword_view response: {serializer.data}")
    return Response({'videos': serializer.data})

@api_view(['GET'])
def get_videos_ordered_by_title_view(request):
    logger.info("get_videos_ordered_by_title_view called")
    videos = Video.objects.order_by("title")
    serializer = VideoSerializer(videos, many=True)
    logger.info(f"get_videos_ordered_by_title_view response: {serializer.data}")
    return Response({'videos': serializer.data})