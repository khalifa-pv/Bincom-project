from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import custom_login_view

urlpatterns = [
    path('', views.image_gallery, name='gallery'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('login/', custom_login_view, name='login'),
]
