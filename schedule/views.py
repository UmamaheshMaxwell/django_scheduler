from django.http import HttpResponse
from django.http import JsonResponse
from google.cloud import scheduler_v1
import os

def index(request):
    return HttpResponse("Here is the page for scheduler")

def get_jobs_list(parent):

    # Create a client
    client = scheduler_v1.CloudSchedulerClient()

    # Initialize request argument(s)
    request = scheduler_v1.ListJobsRequest(parent="projects/gcp-training-386807/locations/us-central1")

    # Make the request
    page_result = client.list_jobs(request=request)

    #Handle the response
    for response in page_result:
        return HttpResponse(response)


def sample_create_job():
    # Create a client
    client = scheduler_v1.CloudSchedulerClient()

    # Initialize request argument(s)
    request = scheduler_v1.CreateJobRequest(parent="projects/gcp-training-386807/locations/us-central1")

    # Make the request
    response = client.create_job(request=request)

    # Handle the response
    return HttpResponse(response)