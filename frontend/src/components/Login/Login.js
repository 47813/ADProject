import React, { useState } from 'react';
import { useEffect } from 'react';
import axios from 'axios';

function LoginForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    axios.get('http://localhost:8000/csrf/', { withCredentials: true });
  }, []);

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const csrftoken = getCookie('csrftoken');
      const response = await axios.post(
        'http://localhost:8000/login/',
        { username, password },
        {
          withCredentials: true,
          headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
          },
        }
      );
      setMessage(response.data.message);
      setIsLoggedIn(true);
    } catch (error) {
      setMessage(error.response?.data?.error || 'Login failed');
    }
  };

  const handleLogout = async () => {
    try {
      const csrftoken = getCookie('csrftoken');
      const response = await axios.post(
        'http://localhost:8000/logout/',
        {},
        {
          withCredentials: true,
          headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
          },
        }
      );
      setMessage(response.data.message);
      setIsLoggedIn(false);
      setUsername('');
      setPassword('');
    } catch (error) {
      setMessage('Logout failed');
    }
  };

  return (
    <div className="container mt-5" style={{ maxWidth: '400px' }}>
      {!isLoggedIn ? (
        <>
          <h2 className="mb-4">로그인</h2>
          <form onSubmit={handleLogin}>
            <div className="mb-3">
              <label className="form-label">사용자명</label>
              <input
                type="text"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">비밀번호</label>
              <input
                type="password"
                className="form-control"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <button className="btn btn-primary w-100" type="submit">
              로그인
            </button>
          </form>
        </>
      ) : (
        <div>
          <h2 className="mb-4">환영합니다! {username}님!</h2>
          <button className="btn btn-danger w-100" onClick={handleLogout}>
            로그아웃
          </button>
        </div>
      )}
      {message && <div className="alert alert-info mt-3">{message}</div>}
    </div>
  );
}

export default LoginForm;