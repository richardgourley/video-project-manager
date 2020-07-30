from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=120)