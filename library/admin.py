from django.contrib import admin
from .models import Book, Author, Language, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
