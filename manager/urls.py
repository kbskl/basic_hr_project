from django.urls import path
from . import views
from .views import home, add_job_post, update_job_post, delete_job_post, detail_job_post, detail_job_application

app_name = "manager"

urlpatterns = [
    path('', home, name="home"),
    path('add/job-post', add_job_post, name="add-job-post"),
    path('update/job-post/<str:jobpost_uuid>', update_job_post, name="update-job-post"),
    path('delete/job-post/<str:jobpost_uuid>', delete_job_post, name="delete-job-post"),
    path('detail/job-post/<str:jobpost_uuid>', detail_job_post, name="detail-job-post"),
    path('detail/job-application/<str:jobapplication_uuid>', detail_job_application, name="detail-job-application"),
]
