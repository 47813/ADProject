# library/tests/test_services.py

import pytest
from library.models import Video
from library.services.video_service import get_video_by_id
from library.exceptions import VideoNotFound

@pytest.mark.django_db
def test_get_video_by_id_success():
    # Given
    video = Video.objects.create(title='Test Video', author='Tester', isbn='1234567890123')

    # When
    result = get_video_by_id(video.id)

    # Then
    assert result == video
    assert result.title == 'Test Video'

@pytest.mark.django_db
def test_get_video_by_id_not_found():
    # When & Then
    with pytest.raises(VideoNotFound) as exc_info:
        get_video_by_id(9999)

    assert "ID 9999에 해당하는 비디오가 없습니다." in str(exc_info.value)