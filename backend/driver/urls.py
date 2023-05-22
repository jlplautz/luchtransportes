# accounts/urls.py
# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from backend.driver import views as v

urlpatterns = [
    path('driver/', v.driver_list, name='driver_list'),
    path('create/', v.driver_create, name='driver_create'),
    path('<int:pk>/', v.driver_detail, name='driver_detail'),
    path('<int:pk>/update/', v.driver_update, name='driver_update'),
]
