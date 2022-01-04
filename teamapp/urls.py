from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('post',views.post,name='post'),
    path('register', views.AccountRegistration.as_view(), name='registration'),
    path('Login',views.Login,name='Login'),
    path("Logout",views.Logout,name="Logout"),
    #path('<int:article_id>/update', views.update, name='update'),
    #path('hello', views.hello, name='hello'),
    #path('redirect', views.redirect_test, name='redirect_test'),
    #path('detail/<int:article_id>/', views.detail, name='detail'),
    #path('<int:article_id>/delete', views.delete, name='delete'),
    #path('<int:article_id>/like',views.like, name='like'),
    #path('api/articles/<int:article_id>/like',views.api_like),
]