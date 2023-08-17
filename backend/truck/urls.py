# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from backend.truck import views as v

app_name = 'truck'

urlpatterns = [
    path('truck/', v.truck_list, name='truck_list'),
    path('truckflue/', v.truckflue_list, name='truckflue_list'),
    path('truckrepair/', v.truckrepair_list, name='truckrepair_list'),
    path('create/', v.truck_create, name='truck_create'),
    path('createflue/', v.truckflue_create, name='truckflue_create'),
    path('createrepair/', v.truckrepair_create, name='truckrepair_create'),
    path('<int:pk>/', v.truck_detail, name='truck_detail'),
    path('<int:pk>/update/', v.truck_update, name='truck_update'),
    path('<int:pk>/delete/', v.truck_delete, name='truck_delete'),
    path('<int:pk>/flueupdate/', v.flueupdate, name='flueupdate'),
    path('<int:pk>/fluedelete/', v.fluedelete, name='fluedelete'),
    path('<int:pk>/repairupdate/', v.repairupdate, name='repairupdate'),
    path('<int:pk>/repairdelete/', v.repairdelete, name='repairdelete'),
]
