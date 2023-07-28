from django.contrib import admin

from parser.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Class for viewing transactions in admin panel"""

    list_display = ('pk', 'name')
    ordering = ('pk', 'name')
    list_per_page = 30
    search_fields = ('pk', 'name')
    list_display_links = ('pk', 'name')
