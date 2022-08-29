from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_wishlist, name='wishlist'),
    path(
        'add_to_wishlist/<int:card_id>', views.add_to_wishlist,
        name='add_to_wishlist'
        ),
]
