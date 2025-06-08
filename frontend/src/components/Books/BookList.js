import React, { useEffect, useState } from 'react';
import axios from 'axios';

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/books/')
      .then(response => setBooks(response.data.books))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">전체 책 목록</h2>
      <div className="mb-4">
        <div className="btn-group" role="group" aria-label="View Options">
          <a href="/books/author/" className="btn btn-outline-primary px-4 py-2">저자별 보기</a>
          <a href="/books/keyword/" className="btn btn-outline-secondary px-4 py-2">키워드로 보기</a>
          <a href="/books/sorted/" className="btn btn-outline-success px-4 py-2">제목순 정렬</a>
        </div>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>제목</th>
            <th>저자</th>
          </tr>
        </thead>
        <tbody>
          {books.map(book => (
            <tr key={book.id}>
              <td>{book.title}</td>
              <td>{book.author}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default BookList;