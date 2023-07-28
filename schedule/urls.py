from django.urls import path 
from . import views 

urlpatterns = [
    path("api/", views.index, name="index"),
    path("api/getjobslist", views.get_jobs_list, name="getjobslist")
]