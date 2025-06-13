from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
import logging

logger = logging.getLogger('books')

@api_view(['GET'])
def get_all_books_view(request):
    logger.info("get_all_books_view called")
    books = Book.get_all_books()
    serializer = BookSerializer(books, many=True)
    logger.info(f"get_all_books_view response: {serializer.data}")
    return Response({'books': serializer.data})

@api_view(['GET'])
def get_books_by_author_view(request, author_name):
    logger.info(f"get_books_by_author_view called with author_name: {author_name}")
    books = Book.objects.filter(author__icontains=author_name)
    serializer = BookSerializer(books, many=True)
    logger.info(f"get_books_by_author_view response: {serializer.data}")
    return Response({'books': serializer.data})

@api_view(['GET'])
def get_books_by_title_keyword_view(request, keyword):
    logger.info(f"get_books_by_title_keyword_view called with keyword: {keyword}")
    books = Book.objects.filter(title__icontains=keyword)
    serializer = BookSerializer(books, many=True)
    logger.info(f"get_books_by_title_keyword_view response: {serializer.data}")
    return Response({'books': serializer.data})

@api_view(['GET'])
def get_books_ordered_by_title_view(request):
    logger.info("get_books_ordered_by_title_view called")
    books = Book.objects.order_by("title")
    serializer = BookSerializer(books, many=True)
    logger.info(f"get_books_ordered_by_title_view response: {serializer.data}")
    return Response({'books': serializer.data})