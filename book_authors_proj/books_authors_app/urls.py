from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),

    path('books', views.books),
    path('books/<int:id>', views.book_view),

    path('authors', views.authors),
    path('authors/<int:id>', views.author_view),
]
