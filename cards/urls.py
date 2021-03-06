from django.urls import path
from cards import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learn/<int:pack_id>', views.view_pack, name='learn'),
    path('create', views.create_pack, name='create'),
    path('edit/<int:pack_id>', views.edit_pack, name='edit'),
    path('delete/<int:pack_id>', views.delete_pack, name='delete'),
    path('like/<int:pk>', views.like_pack, name='like'),
    path('profile/<int:user_id>', views.view_user_profile, name='profile'),
    path('search', views.search, name='search'),
]
