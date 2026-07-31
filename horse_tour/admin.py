from django.contrib import admin
from .models import *
from . import models
# Register your models here.
admin.site.register(models.CategoryHorse)
admin.site.register(models.Horse)
admin.site.register(models.HorseTour)
admin.site.register(models.CommentHorse)
admin.site.register(models.Reservation)


