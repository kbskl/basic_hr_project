from django.urls import path
from .views import home, detail_job_post, apply_job_post, fast_apply_job_post, my_job_application, all_job_post

app_name = "jobseek"

urlpatterns = [
    path('', home, name="home"),
    path('list/my-application', my_job_application, name="list-my-applications"),
    path('list/all-job-post', all_job_post, name="all-job-post"),
    path('detail/job-post/<str:jobpost_uuid>', detail_job_post, name="detail-job-post"),
    path('detail/job-post/<str:jobpost_uuid>/apply', apply_job_post, name="apply-job-post"),
    path('detail/job-post/<str:jobpost_uuid>/fast-apply', fast_apply_job_post, name="apply-fast-job-post"),
]
