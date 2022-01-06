from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('post',views.post,name='post'),
    path('register', views.AccountRegistration.as_view(), name='registration'),
    path('Login',views.Login,name='Login'),
    path("Logout",views.Logout,name="Logout"),

]