from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'account'
urlpatterns = [
    path('', views.dashboard , name='dashboard'),

    # login / logout urls
    path('login/' , auth_views.LoginView.as_view() , name='login'),
    path('logout/' , views.UserLogoutView.as_view(http_method_names=['get' , 'post' , 'options']) , name='logout'),

    # password change urls
    path('password-change/',auth_views.PasswordChangeView.as_view() , name='password_change'),
    path('password-change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done'),
]