from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:id>/edit/', views.user_update, name='user_update'),
    path('<int:id>/delete/', views.user_delete, name='user_delete'),
]
