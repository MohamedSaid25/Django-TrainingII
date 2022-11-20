from django.urls import path
from . import views
from django_filters.views import FilterView
urlpatterns = [

    # path #callFunction #name of function
    path('', views.AlbumViewApprovedList.as_view(), name="albums"),
    path('create', views.CreateForm.as_view(), name='create'),
    path('manualFilter', views.AlbumManualFilter.as_view(), name="manualFilter"),

]
