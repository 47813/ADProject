import React, { useEffect, useState } from 'react';
import axios from 'axios';

function RequestInfo() {
  const [info, setInfo] = useState(null);
  const [error, setError] = useState(null);

  const [getParam, setGetParam] = useState('');
  const [postBody, setPostBody] = useState('');

  const handleGetParamSubmit = () => {
    axios.get(`http://localhost:8000/request_info/?${getParam}/`)
      .then(response => setInfo(response.data))
      .catch(error => {
        setError('GET 요청 실패');
        console.error(error);
      });
  };

  const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === `${name}=`) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  const handlePostBodySubmit = () => {
    const params = new URLSearchParams(postBody);
    axios.post('http://localhost:8000/request_info/', params, {
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      withCredentials: true
    })
    .then(response => setInfo(response.data))
    .catch(error => {
      setError('POST 요청 실패');
      console.error(error);
    });
  };

  useEffect(() => {
    axios.get('http://localhost:8000/request_info/')
      .then(response => {
        setInfo(response.data);
      })
      .catch(error => {
        setError('요청 중 오류가 발생했습니다.');
        console.error(error);
      });
  }, []);

  return (
    <div className="container mt-4">
      <h2>Request Info</h2>
      {error && <p className="text-danger">{error}</p>}
      {info ? (
        <div className="card p-3 bg-light">
          <h5>📥 요청 방식: {info.method}</h5>
          <p><strong>🔗 요청 경로:</strong> {info.path}</p>
          <p><strong>🌐 전체 URL:</strong> {info.full_url}</p>
          <p><strong>🖥️ 클라이언트 IP:</strong> {info.client_ip}</p>
          <p><strong>🧭 User-Agent:</strong> {info.user_agent}</p>
          <hr />
          <h6>🧾 GET 요청 정보</h6>
          <pre>{JSON.stringify(info.get_data, null, 2)}</pre>
          <h6>🧾 POST 요청 정보</h6>
          <pre>{JSON.stringify(info.post_data, null, 2)}</pre>
          <h6>👤 사용자 정보</h6>
          <p>로그인 여부: {info.is_logged_in ? '✅ 로그인됨' : '❌ 로그인 안됨'}</p>
          <p>사용자: {info.user}</p>
          <h6>🍞 세션 데이터</h6>
          <p>{info.session_value}</p>
          <hr />
          <h5 className="mt-4">🔧 요청 테스트</h5>
          <div className="mb-3">
            <label className="form-label">GET 요청 파라미터</label>
            <div className="input-group">
              <input
                type="text"
                className="form-control"
                placeholder="예: test=123"
                value={getParam}
                onChange={e => setGetParam(e.target.value)}
              />
              <button className="btn btn-outline-primary" onClick={handleGetParamSubmit}>GET 전송</button>
            </div>
          </div>

          <div className="mb-3">
            <label className="form-label">POST 요청 내용</label>
            <div className="input-group">
              <input
                type="text"
                className="form-control"
                placeholder="예: name=admin"
                value={postBody}
                onChange={e => setPostBody(e.target.value)}
              />
              <button className="btn btn-outline-success" onClick={handlePostBodySubmit}>POST 전송</button>
            </div>
          </div>
        </div>
      ) : (
        !error && <p>로딩 중...</p>
      )}
    </div>
  );
}

export default RequestInfo;