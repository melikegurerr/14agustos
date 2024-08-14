
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),  
    path("home", views.home), 
    path("books", views.books, name='Kitaplar'),
    path("books/<int:id>", views.bookdetails, name='detaylar'),
]
