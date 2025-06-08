from library.models import Book
from library.exceptions import BookNotFound, BookHasNoBorrowHistory
def get_all_books():
  return Book.objects.all()

def get_book_by_id(book_id: int) -> Book:
  try:
    return Book.objects.get(id=book_id)
  except Book.DoesNotExist:
    raise BookNotFound(f"Book with id {book_id} does not exist")

def get_borrow_history_for_book(book: Book):
  histories = book.borrow_history.order_by("-borrowed_at")
  if not histories:
    raise BookHasNoBorrowHistory(f"No history for book with id {book.title}")
  return histories