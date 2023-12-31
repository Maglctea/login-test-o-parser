from django.urls import path

from parser.views import ListProductsView, DetailProductsView

urlpatterns = [
    path('', ListProductsView.as_view(), name='products'),
    path('<int:pk>/', DetailProductsView.as_view(), name='detail_product')
]