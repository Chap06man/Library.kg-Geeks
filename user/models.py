from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    photo = models.ImageField(upload_to='users/', blank=True)
    phone_number = models.CharField(max_length=15)

    GENDER = (
        ("M", "M"),
        ("Ж", "Ж"),
    )
    gender = models.CharField(max_length=100, choices=GENDER, default="M")
    day_birth = models.DateField()
    location = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    prof = models.CharField(max_length=50)
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return self.username