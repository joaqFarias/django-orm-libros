from django.shortcuts import render, HttpResponse, redirect
from books_authors_app.models import *

def root(request):
    return redirect('/books')

def books(request):
    if request.method == 'POST':
        libro_new = Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        libro_new.save() 

    libros = Book.objects.all()
    context = {
        'libros': libros,
    }
    return render(request, 'books.html', context)

def book_view(request, id):
    libro_id = Book.objects.get(id=int(id))

    if request.method == 'POST':
        autor_get = Author.objects.get(id=int(request.POST['autor_get']))
        libro_id.author.add(autor_get)

    autores = libro_id.author.all()

    excludes = []
    for ex in Author.objects.all():
        if ex in autores:
            excludes.append(ex.first_name)
    autores_out = Author.objects.exclude(first_name__in=excludes)

    context = {'libro': libro_id, 'autores': autores, 'autores_out': autores_out}

    return render(request, 'book_view.html', context)



def authors(request):
    if request.method == 'POST':
        autor_new = Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
        autor_new.save() 

    autores = Author.objects.all()
    context = {
        'autores': autores,
    }
    return render(request, 'authors.html', context)

def author_view(request, id):
    autor_id = Author.objects.get(id=int(id))

    if request.method == 'POST':
        libro_get = Book.objects.get(id=int(request.POST['libro_get']))
        autor_id.books.add(libro_get)

    libros = autor_id.books.all()

    excludes = []
    for ex in Book.objects.all():
        if ex in libros:
            excludes.append(ex.title)
    libros_out = Book.objects.exclude(title__in=excludes)

    context = {'autor': autor_id, 'libros': libros, 'libros_out': libros_out}

    return render(request, 'author_view.html', context)

