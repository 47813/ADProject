import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import VideoList from './components/Videos/VideoList';
import VideoSearchByAuthor from './components/Videos/VideoSearchByAuthor';
import VideoSearchByKeyword from './components/Videos/VideoSearchByKeyword';
import VideoSortedByTitle from "./components/Videos/VideoSortedByTitle";
import RequestInfo from "./components/RequestTest/RequestInfo";
import LoginForm from "./components/Login/Login";
import HelloAPIApp from "./components/DRFTest/Hello";
import MainScreen from "./components/MainScreen/MainScreen";
// 다른 컴포넌트 import 예정

function App() {
  return (
    <Router>
      <Routes>
          <Route path="/videos" element={<VideoList />} />
          <Route path="/videos/author" element={<VideoSearchByAuthor />} />
          <Route path="/videos/keyword" element={<VideoSearchByKeyword />} />
          <Route path="/videos/sorted" element={<VideoSortedByTitle />} />
          <Route path="/request_info" element={<RequestInfo />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/hello" element={<HelloAPIApp />} />
          <Route path="/" element={<MainScreen />} />
        {/* /videos 하위 author, keyword, sorted 경로 */ }
      </Routes>
    </Router>
  );
}

export default App;