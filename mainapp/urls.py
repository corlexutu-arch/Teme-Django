from django.urls import path
from mainapp import views

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("movies/", views.movies_view, name="movies"),
    path("books/", views.books_view, name="books"),
    path("tema29/", views.tema29_view, name="tema29"),
    path("movies/add", views.add_movie, name="add-m"),
    path("movies/<id>", views.m_details, name="m_details"),
    path("books/add", views.add_book, name="add-b"),
    path("books/<id>", views.b_details, name="b_details"),
    path("books/update/<int:id>/", views.update_book, name="update_book"),
]
