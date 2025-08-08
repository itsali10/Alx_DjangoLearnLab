from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]

