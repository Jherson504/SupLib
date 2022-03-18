from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('sign-in/', views.login_page, name='sign-in'),

]
