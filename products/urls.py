from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cards, name='products'),
    path('<card_id>', views.card_detail, name='card_detail'),
]
