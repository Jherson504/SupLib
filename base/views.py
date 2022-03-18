from django.shortcuts import render
from .models import Book


def home(request):
    __books = Book.objects.all()
    context = {'books': __books}
    return render(request, 'base/home.html', context)
