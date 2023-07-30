from django.http import HttpResponse
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

    # Handle the response
    # for response in page_result:
    #     return HttpResponse(response)
    response_data = [str(response) for response in page_result]
    return HttpResponse("\n".join(response_data))