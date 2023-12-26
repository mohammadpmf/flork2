from django.db import models


class Book(models.Model):
    title = models.CharField(max_length = 60)
    author = models.CharField(max_length = 100)
    translator = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True)
    
    def __str__(self):
        return f"{self.author}: {self.title}"

