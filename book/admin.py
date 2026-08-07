from django.contrib import admin
from .models import Book
from . import models

# 2-Домашка.-----------------------------------------------
# @admin.register(models.Book)
# 6-Домашка------------------------------------------------
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('views',)