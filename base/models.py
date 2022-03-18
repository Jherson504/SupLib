from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created', ]


class Book(models.Model):

    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    topics = models.ManyToManyField(Topic)
    description = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created', '-updated']


class Article(models.Model):

    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created', 'updated']

    def __str__(self):
        return f"{self.book.title}/{self.name}/"


class Section(models.Model):

    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created', 'updated']
