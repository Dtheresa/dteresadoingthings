from django.conf import settings
from django.db import models
from django.utils import timezone


class Author(models.Model):
    TITLE_CHOICES = [('MR', 'Mr.'),
                     ('MRS', 'Mrs.'),
                     ('MS', 'Ms.'),
                     ('DR', 'Dr'),
                     ('SIR', 'Sir')]
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField(
        help_text='Enter a brief description about the Author', default="")
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', blank=True, null=True)

    # def __init__(self, arg):
    #   super(Author, self).__init__()
    #   self.arg = arg

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre


class Language(models.Model):
    language = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.language


class Book(models.Model):
    author = models.ManyToManyField(Author)
    title = models.CharField(max_length=400)
    summary = models.TextField(
        help_text='Enter a brief description of the book', default="")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    language = models.ManyToManyField(Language)
    genre = models.ManyToManyField(Genre)
    page_count = models.IntegerField(default=0)

    def __str__(self):
        # return self.title
        return '{} - {} {}'.format(
            self.title, self.author.first_name, self.author.last_name)
