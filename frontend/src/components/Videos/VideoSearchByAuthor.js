import axios from 'axios';
import React, { useState } from 'react';

function VideoSearchByAuthor() {
  const [searchTerm, setSearchTerm] = useState('');
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (searchTerm.trim() === '') return;

    setLoading(true);
    setError(null);

    try {
      const response = await axios.get(
        `http://localhost:8000/videos/author/${encodeURIComponent(searchTerm.trim())}/`
      );
      setVideos(response.data.videos || []);
    } catch (err) {
      setError('데이터를 불러오지 못했습니다.');
      setVideos([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-4">감독으로 비디오 검색</h2>
      <form onSubmit={handleSubmit} className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="저자명을 입력하세요"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button className="btn btn-primary" type="submit">검색</button>
      </form>

      {loading && <p>불러오는 중...</p>}
      {error && <p className="text-danger">{error}</p>}

      {videos.length > 0 && (
        <table className="table table-striped mt-4">
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
      )}
    </div>
  );
}

export default VideoSearchByAuthor;