from django.shortcuts import render
from django.http import HttpResponseNotFound
from library.services import video_service
from library.exceptions import VideoNotFound, VideoHasNoBorrowHistory
import logging

logger = logging.getLogger('library')

def video_list(request):
  logger.info("video_list called")
  videos = video_service.get_all_videos()
  return render(request, 'library/video_list.html', {'videos': videos})

def video_history(request, video_id):
  logger.info(f"video_history called with video_id: {video_id}")
  try:
    video = video_service.get_video_by_id(video_id)
    histories = video_service.get_borrow_history_for_video(video)
  except VideoNotFound as e:
    logger.warning(f"video_history response: {str(e)}")
    return HttpResponseNotFound(str(e))
  except VideoHasNoBorrowHistory as e:
    logger.warning(f"video_history response: {str(e)}")
    return render(request, "library/no_history.html", {"message": str(e)})
  logger.info(f"video_history response: {video}")
  return render(request, 'library/video_history.html', {'video': video, 'histories': histories})