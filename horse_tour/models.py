from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.---------------------------------------------
class CategoryHorse(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Reservation(models.Model):
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return self.location

    class Meta:
            verbose_name = 'Бронь'
            verbose_name_plural = 'Броня'

class Horse(models.Model):
    name = models.CharField(max_length=20,null=True)
    category = models.ManyToManyField(CategoryHorse,blank=True)
    location = models.ForeignKey(Reservation,on_delete=models.CASCADE,related_name="horses")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Конь'
        verbose_name_plural = 'Кони'

class HorseTour(models.Model):
    person = models.CharField(max_length=30,null=False)
    adress = models.OneToOneField(Reservation, blank=True, on_delete=models.CASCADE )

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = "Конный тур"
        verbose_name_plural = "Конные туры"

class CommentHorse(models.Model):
    person = models.CharField(max_length=30)
    text = models.TextField()
    location = models.ForeignKey(Reservation,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = "Комент"
        verbose_name_plural = "Комент"