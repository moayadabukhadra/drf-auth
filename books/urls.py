from django.urls import path
from books.api.viewset import (
                                BooksListAPIView,
                                BooksDetailAPIView
                                )
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/v1/books-list', BooksListAPIView.as_view(), name='books_list'),
    path('api/v1/<int:pk>', BooksDetailAPIView.as_view(), name='book_detail'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]



