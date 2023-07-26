from django.db import models


class Product(models.Model):
    """Product model"""

    title = models.CharField(verbose_name='title', max_length=50)
    url_product = models.URLField(verbose_name='url')
    url_photo = models.URLField(verbose_name='photo')
    price = models.PositiveIntegerField(verbose_name='price')

    def __str__(self):
        return self.title
