# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from backend.freight import views as v

urlpatterns = [
    path('freight/', v.freight_list, name='freight_list'),
    path('create/', v.freight_create, name='freight_create'),
    path('<int:pk>/', v.freight_detail, name='freight_detail'),
    path('<int:pk>/update/', v.freight_update, name='freight_update'),
]
