# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from backend.freight import views as v

app_name = 'freight'

urlpatterns = [
    # path('freight/', v.FreightListView.as_view(), name='freight_list'),
    path('freight/', v.freight_list, name='freight_list'),
    path('freightfee/', v.freightfee_list, name='freightfee_list'),
    path('create/', v.freight_create, name='freight_create'),
    path('createfee/', v.freightfee_create, name='freightfee_create'),
    path('<int:pk>/', v.freight_detail, name='freight_detail'),
    path('<int:pk>/delete/', v.freight_delete, name='freight_delete'),
    path('<int:pk>/update/', v.freight_update, name='freight_update'),
    path('<int:pk>/feeupdate/', v.feeupdate, name='feeupdate'),
    path('<int:pk>/feedelete/', v.feedelete, name='feedelete'),
]
