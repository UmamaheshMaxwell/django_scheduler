import uuid
from django.http import HttpResponse
from django.http import JsonResponse
from google.cloud import scheduler_v1
import os

def index(request):
    return HttpResponse("Here is the page for scheduler")

def list_jobs(parent):

    # Create a client
    client = scheduler_v1.CloudSchedulerClient()

    # Initialize request argument(s)
    request = scheduler_v1.ListJobsRequest(parent="projects/gcp-training-386807/locations/us-central1")

    # Make the request
    page_result = client.list_jobs(request=request)

    #Handle the response
    for response in page_result:
        return HttpResponse(response)

def make_job():
    # Create a client
    client = scheduler_v1.CloudSchedulerClient()

    # Generate a unique job name using a combination of timestamp and random string
    job_name = f"djnago-app-job-{uuid.uuid4().hex}"

    # Initialize request argument(s) with the generated job name
    request = scheduler_v1.CreateJobRequest(parent="projects/gcp-training-386807/locations/us-central1", job={"name": job_name})

    # Make the request
    response = client.create_job(request=request)

    # Handle the response
    return HttpResponse(response)