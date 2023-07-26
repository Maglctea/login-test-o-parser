from django.contrib import admin

from parser.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Class for viewing transactions in admin panel"""

    list_display = ('pk', 'title', 'price')
    # list_filter = ('type',)
    ordering = ('pk', 'title', 'price')
    list_per_page = 30
    search_fields = ('pk', 'title')
    list_display_links = ('pk', 'title')