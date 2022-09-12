from django.urls import path

from . import views
from user.views import  UserRegisterApiView,UserLoginApi

urlpatterns = [
    path('register/', UserRegisterApiView.as_view(),name="register_api"),
    path('user_login/', UserLoginApi.as_view(), name="log_in")

]