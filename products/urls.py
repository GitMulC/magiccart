from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cards, name='products'),
    path('<int:card_id>', views.card_detail, name='card_detail'),
    path('add/', views.add_card, name='add_card'),
]
