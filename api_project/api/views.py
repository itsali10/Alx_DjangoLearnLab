from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()        # All books from DB
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]    # Convert to JSON


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]