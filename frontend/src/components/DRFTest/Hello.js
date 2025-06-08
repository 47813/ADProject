

import React, { useState } from 'react';
import axios from 'axios';

function HelloAPIApp() {
  const [getMessage, setGetMessage] = useState('');
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');
  const [postResponse, setPostResponse] = useState('');

  const handleGet = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/hello/');
      setGetMessage(response.data.message);
    } catch (error) {
      setGetMessage('GET request failed');
    }
  };

  const handlePost = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/post/', {
        name,
        message,
      });
      setPostResponse(response.data.message);
    } catch (error) {
      setPostResponse(error.response?.data?.message || 'POST request failed');
    }
  };

  return (
    <div className="container mt-5">
      <h2>Hello API Test</h2>

      <button className="btn btn-primary mb-3" onClick={handleGet}>
        Send GET Request
      </button>
      {getMessage && <p>{getMessage}</p>}

      <form onSubmit={handlePost}>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <input
            type="text"
            className="form-control"
            placeholder="Message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-success">
          Send POST Request
        </button>
      </form>
      {postResponse && <p className="mt-3">{postResponse}</p>}
    </div>
  );
}

export default HelloAPIApp;