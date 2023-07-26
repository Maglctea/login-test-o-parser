from django.urls import path

from parser.views import ListProductsView, DetailProductsView

urlpatterns = [
    path('', ListProductsView.as_view()),
    path('<int:pk>/', DetailProductsView.as_view())
]