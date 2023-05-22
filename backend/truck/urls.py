# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from backend.truck import views as v

urlpatterns = [
    path('truck/', v.truck_list, name='truck_list'),
    path('create/', v.truck_create, name='truck_create'),
    path('<int:pk>/', v.truck_detail, name='truck_detail'),
    path('<int:pk>/update/', v.truck_update, name='truck_update'),
]
