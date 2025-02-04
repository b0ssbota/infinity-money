
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.signout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]
