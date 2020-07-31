from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=120)
    homepage_image = models.FileField(null=True, blank=True, upload_to="files")
    homepage_text = models.TextField(max_length=1000)
    category_page_text = models.TextField(max_length=1000)
    slug = models.SlugField(default="fishing", help_text="This is how this category page appears in the browser. No spaces, please use an underscore (_) between words.")

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

    PLACEMENT = (
        ('h', 'Home Page'),
        ('c', 'Category Page')
    )

    placement = models.CharField(
        max_length=1,
        choices=PLACEMENT,
        blank=False,
        default='c',
        help_text='Choose whether to place a video on home page, dedicated content page OR as featured video (top of dedicted content page)'
    )

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    class Meta:
        verbose_name = 'testimonial'
        verbose_name_plural = 'testimonials'
    client_name = models.CharField(max_length=120)
    comment = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.client_name




