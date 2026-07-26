from django.db import models

#Домашка-2
class Book(models.Model):
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=150)
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title