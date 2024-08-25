from django.urls import path,include
from . import views

app_name="chef"
urlpatterns = [
    path("signup/",views.signup_user,name="signup_user"),
    path("login/",views.login_user,name="login_user"),
    path("account/",views.account,name="account")
]
