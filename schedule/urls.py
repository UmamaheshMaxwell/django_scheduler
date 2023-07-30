from django.urls import path 
from . import views 

urlpatterns = [
    path("api/", views.index, name="index"),
    path("api/listjobs", views.list_jobs, name="listjobs"),
    path("api/makejob", views.make_job, name="makejob")
]