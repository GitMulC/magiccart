from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cards, name='products'),
    path('<int:card_id>/', views.card_detail, name='card_detail'),
    path('add/', views.add_card, name='add_card'),
    path('edit/<int:card_id>/', views.edit_card, name='edit_card'),
    path('delete/<int:card_id>/', views.delete_card, name='delete_card'),
]
