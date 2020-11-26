from django.urls import path, include
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, UpdateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('update_profile/', UserEditView.as_view(), name='update_profile'),
    path('password/', PasswordsChangeView.as_view(), name='update_password'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/update_profile_page/', UpdateProfilePageView.as_view(), name='update_profile_page'),
]
