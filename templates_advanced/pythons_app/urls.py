from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('login/', views.sign_in, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
