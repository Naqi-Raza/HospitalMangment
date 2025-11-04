from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('appointment', views.appointment, name='appointment'),
    path('slip', views.slip, name='bookingslip'),
    path('userpage',views.userpage, name='userpage'),
    path('Drlist',views.Drlist, name='Drlist'),
]
