from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length = 60, verbose_name="عنوان")
    author = models.CharField(max_length = 100, verbose_name="نویسنده")
    translator = models.CharField(max_length=100, blank=True, verbose_name="مترجم")
    publisher = models.CharField(max_length=100, blank=True, verbose_name="ناشر")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="قیمت")
    description = models.TextField(verbose_name="توضیحات")
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name="عکس کتاب")
    
    def __str__(self):
        return f"{self.author}: {self.title}"


class Comment(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, verbose_name='نام کتاب')
    name = models.CharField(max_length = 60, verbose_name="نام نظر دهنده", blank=True)
    email = models.EmailField(max_length = 100, verbose_name="آدرس ایمیل نظر دهنده", blank=True)
    text = models.TextField(verbose_name="متن نظر")

    def __str__(self):
        return self.text

