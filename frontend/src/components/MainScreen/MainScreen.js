import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const MainScreen = () => {
  const [description] = useState("이 앱은 Django 백엔드와 통신하는 React 프론트엔드 예제입니다. 다양한 기능을 통해 Django REST API와의 상호작용을 실습할 수 있습니다.");

  return (
    <div className="container mt-4">
      <h2>📚 React + Django 실습 데모 페이지</h2>
      <div className="alert alert-secondary">
        {description}
      </div>
      <p className="text-muted">
        이 페이지는 Django REST API와 통신하는 React 앱들로 구성되어 있습니다. 각각의 기능을 아래에서 확인해보세요.
      </p>

      <ul className="list-group">
        <li className="list-group-item">
          🔐 <strong>로그인 시스템</strong> – 사용자 로그인 및 로그아웃
          <br />
          <Link to="/login" className="btn btn-sm btn-primary mt-2">Login 컴포넌트 이동</Link>
        </li>
        <li className="list-group-item">
          📡 <strong>요청 정보 확인</strong> – 요청 메서드, 유저 정보, 세션 정보 등을 출력
          <br />
          <Link to="/request_info" className="btn btn-sm btn-info mt-2">RequestInfo 컴포넌트 이동</Link>
        </li>
        <li className="list-group-item">
          🎬 <strong>전체 비디오 목록</strong> – 비디오 출력 및 필터 적용
          <br />
          <Link to="/videos" className="btn btn-sm btn-secondary mt-2">VideoList 이동</Link>
        </li>
        <li className="list-group-item">
          🌐 <strong>Hello API</strong> – 간단한 GET 테스트
          <br />
          <Link to="/hello" className="btn btn-sm btn-outline-primary mt-2">Hello 컴포넌트 이동</Link>
        </li>
      </ul>
    </div>
  );
};

export default MainScreen;