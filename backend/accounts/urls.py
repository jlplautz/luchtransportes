# accounts/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from backend.accounts import views as v

user_patterns = [
    path('', v.user_list, name='user_list'),
    path('create/', v.user_create, name='user_create'),
    path('<int:pk>/', v.user_detail, name='user_detail'),
    path('<int:pk>/update/', v.user_update, name='user_update'),
    path('<int:pk>/delete/', v.user_delete, name='user_list'),
]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', v.signup, name='signup'),
    path(
        'reset/<uidb64>/<token>/',
        v.MyPasswordResetConfirm.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        v.MyPasswordResetComplete.as_view(),
        name='password_reset_complete',
    ),
    path('users/', include(user_patterns)),
]
