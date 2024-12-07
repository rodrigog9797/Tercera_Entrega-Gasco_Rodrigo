from django.contrib import admin
from django.urls import path, include
from Users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='Users/logout.html'), name='Logout'),

]   