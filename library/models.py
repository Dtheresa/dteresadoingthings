from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    summary = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    page_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
