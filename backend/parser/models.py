from django.db import models


class Product(models.Model):
    """Product model"""

    name = models.CharField(verbose_name='title', max_length=50)
    url = models.URLField(verbose_name='url')

    def __str__(self):
        return self.name
