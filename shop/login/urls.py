from django.urls import path
from . import views

urlpatterns = [
    path("sign_in",views.sign_in, name="sign_in"),#sign_in
    path("",views.logining, name="login"),#login
    


]
