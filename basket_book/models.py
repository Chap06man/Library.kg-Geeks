from django.db import models
from book.models import Book
from django.core.validators import MinValueValidator, MinLengthValidator
# Create your models here.

class BasketBook(models.Model):
    STATUS = (
        ("Не выполнено","Не выполнено"),
        ("В Обработке", "В Обработке"),
        ("Выполнено", "Выполнено")
    )
    name_order = models.CharField(max_length=50)
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    age = models.PositiveIntegerField(validators=[MinValueValidator(14)])
    card = models.CharField(max_length=16,validators=[MinLengthValidator(16)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS)
