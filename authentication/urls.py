from django.urls import path
from .views import RegistrationView, LoginView
from knox import views as knox_views


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', knox_views.LogoutView.as_view(), name="Logout"),
    path('login/', LoginView.as_view(), name='login'),

]
