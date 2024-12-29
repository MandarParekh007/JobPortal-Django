from django.urls import path
from .views import register,login_view,home_view,logout_view

urlpatterns = [
    path('register/',register,name="reguister"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view, name="logout"),
    path('home/',home_view,name='home')
]