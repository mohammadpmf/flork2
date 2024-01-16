from django.db import models


class Book(models.Model):
    title = models.CharField(max_length = 60, verbose_name="عنوان")
    author = models.CharField(max_length = 100, verbose_name="نویسنده")
    translator = models.CharField(max_length=100, blank=True, verbose_name="مترجم")
    publisher = models.CharField(max_length=100, blank=True, verbose_name="ناشر")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="قیمت")
    description = models.TextField(verbose_name="توضیحات")
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name="عکس کتاب")
    
    def __str__(self):
        return f"{self.author}: {self.title}"

