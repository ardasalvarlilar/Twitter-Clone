from django.urls import path
from .views import *
urlpatterns = [
  path('register/',register_view,name="register_page"),
  path('login/',login_view,name="login_page"),
  path('logout/',logout_view,name='logout_page'),
]
