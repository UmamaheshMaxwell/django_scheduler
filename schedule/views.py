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

    # Process the response data
    job_list = []
    for response in page_result:
        # Convert each job into a dictionary
        job_data = { 
            "name": response.name,
            "http_method": response.http_method,
            "http_target": response.http_target,
            "schedule": response.schedule,
            "time_zone": response.time_zone,
            "state": response.state,
            "user_update_time": response.user_update_time,
            "status": response.status,
            "schedule_time": response.schedule_time,
            "last_attempt_time": response.last_attempt_time,
            "retry_config": response.retry_config,
            "attempt_deadline": response.attempt_deadline            
            }
        job_list.append(job_data)

    # Return the response as JSON
    return JsonResponse(job_list, safe=False)

# def get_jobs_list(parent):

#     # Create a client
#     client = scheduler_v1.CloudSchedulerClient()

#     # Initialize request argument(s)
#     request = scheduler_v1.ListJobsRequest(parent="projects/gcp-training-386807/locations/us-central1")

#     # Make the request
#     page_result = client.list_jobs(request=request)

#     #Handle the response
#     for response in page_result:
#         return HttpResponse(response)


def sample_create_job():
    # Create a client
    client = scheduler_v1.CloudSchedulerClient()

    # Initialize request argument(s)
    request = scheduler_v1.CreateJobRequest(parent="projects/gcp-training-386807/locations/us-central1")

    # Make the request
    response = client.create_job(request=request)

    # Handle the response
    return HttpResponse(response)