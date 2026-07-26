from django.contrib import admin
from .models import Book
from . import models

# 2-Домашка.-----------------------------------------------
admin.site.register(models.Book)
