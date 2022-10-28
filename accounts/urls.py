from django.urls import path
from . import views
urlpatterns = [

    # path #callFunction #name of function
    path('register', views.RegistrationForm.as_view(), name='register'),
    path('login', views.LoginPageView.as_view(), name='login')

]
