import uuid
from django.http import HttpResponse
from django.http import JsonResponse
from google.cloud import scheduler_v1
from google.protobuf.json_format import MessageToDict

def index(request):
    return HttpResponse("Here is the page for scheduler")

def list_jobs(parent):

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
                "description": response.description,
                "schedule": response.schedule,
                "time_zone": response.time_zone,
                "state": "Enabled" if response.state == 1 else "Disabled",
                #"http_target": MessageToDict(response.http_target)
        }
        job_list.append(job_data)

    # Return the response as JSON
    return JsonResponse(job_list, safe=False)


def make_job(parent):
    # Create a client
    client = scheduler_v1.CloudSchedulerClient()

    # Generate a unique job name using a combination of timestamp and random string
    job_id = f"djnago-app-job-{uuid.uuid4().hex}"

    # Initialize request argument(s) with the correct job name format
    project_id = "gcp-training-386807"  # Replace with your actual project ID
    location_id = "us-central1"  # Replace with your desired location ID
    location_name = f"projects/{project_id}/locations/{location_id}"
    job_name = f"projects/{project_id}/locations/{location_id}/jobs/{job_id}"

   # Specify the target for the job (HTTP target in this example)
    http_target = scheduler_v1.HttpTarget(
        uri="https://django-scheduler-3imv474m7a-uc.a.run.app/schedule/api/",
        http_method=scheduler_v1.HttpMethod.GET,
    )

    # Specify the schedule and time zone for the job
    schedule = "0 */1 * * *"  # Every minute schedule
    time_zone = "Asia/Kolkata"  # Time zone for Tokyo, Japan
    #time_zone = "Europe/Brussels"  # Time zone for Belgium

    # Initialize the job with the provided target, schedule, and time zone
    job = scheduler_v1.Job(
        name=job_name,
        description="managed by system",
        http_target=http_target,
        schedule=schedule,
        time_zone=time_zone,
        # Add other job configuration parameters as needed
    )

    request = scheduler_v1.CreateJobRequest(parent=location_name,job=job)
    # Make the request
    response = client.create_job(request=request)

    # Handle the response
    return HttpResponse(response)