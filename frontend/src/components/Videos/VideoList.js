import React, { useEffect, useState } from 'react';
import axios from 'axios';

function VideoList() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/videos/')
      .then(response => setVideos(response.data.videos))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">전체 비디오 목록</h2>
      <div className="mb-4">
        <div className="btn-group" role="group" aria-label="View Options">
          <a href="/videos/author/" className="btn btn-outline-primary px-4 py-2">감독별 보기</a>
          <a href="/videos/keyword/" className="btn btn-outline-secondary px-4 py-2">키워드로 보기</a>
          <a href="/videos/sorted/" className="btn btn-outline-success px-4 py-2">제목순 정렬</a>
        </div>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>제목</th>
            <th>감독</th>
          </tr>
        </thead>
        <tbody>
          {videos.map(video => (
            <tr key={video.id}>
              <td>{video.title}</td>
              <td>{video.author}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default VideoList;