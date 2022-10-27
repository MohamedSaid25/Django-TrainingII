from django.urls import path
from . import views
urlpatterns = [

    # path #callFunction #name of function
    path('create', views.CreateForm.as_view(), name='create')

]
