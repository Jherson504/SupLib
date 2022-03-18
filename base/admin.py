from nntplib import ArticleInfo
from django.contrib import admin
from .models import Article, Book, Section, Tag, Topic


admin.site.register(Article)
admin.site.register(Book)
admin.site.register(Section)
admin.site.register(Tag)
admin.site.register(Topic)
