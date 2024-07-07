
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
   path("signup/", views.SignUp, name="signup"),
   # path("Login/", views.userlogin, name="Login"),
   path("Login/", views.Userloginview.as_view(), name="Login"),
   path("profile/", views.profile, name="profile"),
   path("profile/edit/", views.updateprofile, name="updateprofile"),
   path("logout/", views.userlogout, name="logout"),
   # path("logout/", views.Userlogoutview.as_view(), name="logout"),
   path("profile/passchange", views.passchange, name="passchange"),
]
