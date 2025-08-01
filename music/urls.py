from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_list, name='track_list'),
    path('track/create/', views.track_create, name='track_create'),
    path('track/<int:pk>/', views.track_detail, name='track_detail'),
    path('track/<int:pk>/update/', views.track_update, name='track_update'),
    path('track/<int:pk>/delete/', views.track_delete, name='track_delete'),
]