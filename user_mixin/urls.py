from django.urls import path
from . import views

urlpatterns = [
    path('user_mixin/', views.UserMixin.as_view(),name='user_mixin'),

]