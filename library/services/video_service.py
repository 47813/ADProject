from library.models import Video
from library.exceptions import VideoNotFound, VideoHasNoBorrowHistory

def get_all_videos():
  return Video.objects.all()

def get_video_by_id(video_id: int) -> Video:
  try:
    return Video.objects.get(id=video_id)
  except Video.DoesNotExist:
    raise VideoNotFound(f"Video with id {video_id} does not exist")

def get_borrow_history_for_video(video: Video):
  histories = video.borrow_history.order_by("-borrowed_at")
  if not histories:
    raise VideoHasNoBorrowHistory(f"No history for video with id {video.title}")
  return histories