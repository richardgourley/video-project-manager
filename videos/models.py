from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Project(models.Model):
	class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
    name = models.CharField(max_length=120)
    video_code = models.CharField('YOUTUBE VIDEO CODE: DONT enter the full url, eg. If the URL is https://www.youtube.com/watch?v=h5EtMD1mDiw - Enter h5EtMD1mDiw', max_length=25, null=False)
    order = models.IntegerField('ORDER: (Optional): Videos appear in order on pages, lowest number first. Leave default if order is not important.', default=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)

class Testimonial(models.Model):
    client_name = models.CharField(max_length=120)
    comment = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)