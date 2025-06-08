from django.shortcuts import render
from django.http import HttpResponseNotFound
from library.services import book_service
from library.exceptions import BookNotFound, BookHasNoBorrowHistory
import logging

logger = logging.getLogger('library')

def book_list(request):
  logger.info("book_list called")
  books = book_service.get_all_books()
  return render(request, 'library/book_list.html', {'books':books})

def book_history(request, book_id):
  logger.info(f"book_history called with book_id: {book_id}")
  try:
    book = book_service.get_book_by_id(book_id)
    histories = book_service.get_borrow_history_for_book(book)
  except BookNotFound as e:
    logger.warning(f"book_history response: {str(e)}")
    return HttpResponseNotFound(str(e))
  except BookHasNoBorrowHistory as e:
    logger.warning(f"book_history response: {str(e)}")
    return render(request, "library/no_history.html", {"message": str(e)})
  logger.info(f"book_history response: {book}")
  return render(request, 'library/book_history.html', {'book':book, 'histories':histories})