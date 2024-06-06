
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage),
    path('product/<str:slug>/', views.ProductViewPage, name='ProductViewPage'),
]
