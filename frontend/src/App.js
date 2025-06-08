import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import BookList from './components/Books/BookList';
import BookSearchByAuthor from './components/Books/BookSearchByAuthor';
import BookSearchByKeyword from './components/Books/BookSearchByKeyword';
import BookSortedByTitle from "./components/Books/BookSortedByTitle";
import RequestInfo from "./components/RequestTest/RequestInfo";
import LoginForm from "./components/Login/Login";
import HelloAPIApp from "./components/DRFTest/Hello";
import MainScreen from "./components/MainScreen/MainScreen";
// 다른 컴포넌트 import 예정

function App() {
  return (
    <Router>
      <Routes>
          <Route path="/books" element={<BookList />} />
          <Route path="/books/author" element={<BookSearchByAuthor />} />
          <Route path="/books/keyword" element={<BookSearchByKeyword />} />
          <Route path="/books/sorted" element={<BookSortedByTitle />} />
          <Route path="/request_info" element={<RequestInfo />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/hello" element={<HelloAPIApp />} />
          <Route path="/" element={<MainScreen />} />
        {/* 여기에 author, keyword, sorted 등 경로 추가 가능 */}
      </Routes>
    </Router>
  );
}

export default App;