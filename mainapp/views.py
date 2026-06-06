from django.shortcuts import render, redirect
from datetime import date
from mainapp.models import Movie, Book


def homepage (request):
    movies = Movie.objects.all()
    return render (request, "mainapp/home.html",{"filme": movies})

def m_details (request, id):
    movie = Movie.objects.get(id=id)
    return render (request, "mainapp/m_detail.html", {"movie":movie})

def b_details (request, id):
    book = Book.objects.get(id=id)
    return render (request, "mainapp/b_detail.html", {"book":book})

def movies_view(request):
    movies = Movie.objects.all()
    movies_f = Movie.objects.filter(genre = "action")
    return render (request, "mainapp/movies.html",{"filme":movies,'filme_f':movies_f})

def books_view(request):
    books = Book.objects.all()
    books_f = Book.objects.filter(release_date__year = 2004)
    return render (request, "mainapp/books.html", {"carti":books, "carti_f":books_f})

def tema29_view(request):
    useri ={"Andrei":5,"Paul":2, "Maria":7,"Ana":1}
    return render (request, "mainapp/exercitiu.html",{"useri":useri})

def add_movie (request):
    Movie.objects.create(
        title = "Desperado",
        genre = "action",
        description = "boom boom, pac pac pe muzica latino",
        release_date = date(1995, 1, 1)
    )
    Movie.objects.create(
        title = "Ace Ventura",
        genre = "comedy",
        description = "detectivu lu peste",
        release_date = date(1994, 1, 1)
    )
    Movie.objects.create(
        title = "Pretty women",
        genre = "romance",
        description = "banii nu aduc fericirea dar o intretin",
        release_date = date(1990, 1, 1 )
    )
    Movie.objects.create(
        title = "The Punisher",
        genre = "action",
        description = "pe ei pe familia lor",
        release_date = date(2004, 1, 1)
    )
    return redirect ("movies")


def add_book (request):
    Book.objects.create(
        title = "The Little Prince",
        author = "Antoine de Saint-Exupéry",
        category = "children",
        release_date = date(1943, 1, 1)
    )
    Book.objects.create(
        title = "An autobiography",
        author = "Agatha Christie",
        category = "biography",
        release_date = date(1977, 1, 1)
    )
    Book.objects.create(
        title = "Dexter",
        author = "Jeff Lindsay",
        category = "thriller",
        release_date = date(2004, 1, 1)
    )
    Book.objects.create(
        title = "The Dark Tower",
        author = "Stephen King",
        category = "fantasy",
        release_date = date(2004, 1, 1)
    )
    return redirect ("books")

def update_book(request, id):
    new_title = request.GET.get('nume_nou')
    book = Book.objects.filter(id=id).first()
    if book:
        old_title = book.title
        book.title = new_title
        book.save()
        mesaj = f"Succes! Cartea cu ID {id} are acum titlul: {book.title}"
    return render(request, "mainapp/home.html", {"mesaj_succes": mesaj})