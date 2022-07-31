from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from core.models import JobPost, JobApplication
from general.utility.decorators import manager_required
from general.utility.enums import ActivityStatusTypeEnum
from manager.forms import JobPostForm, JobApplicationDetailForm


@login_required
@manager_required
def home(request):
    context = {
        "all_posts": JobPost.objects.get_all(request.user),
        "jobpost_form": JobPostForm()
    }
    return render(request, "manager/home.html", context)


@login_required
@manager_required
def add_job_post(request):
    if request.POST and 'jobPostSubmit' in request.POST:
        jobpost_form = JobPostForm(request.POST)
        if jobpost_form.is_valid():
            jobpost = jobpost_form.save(commit=False)
            jobpost.employer = request.user
            jobpost.save()
    return redirect('manager:home')


@login_required
@manager_required
def update_job_post(request, jobpost_uuid):
    jobpost = JobPost.objects.get_with_uuid(jobpost_uuid, request.user)
    if jobpost is None:
        return HttpResponseNotFound()
    jobpost_form = JobPostForm(instance=jobpost)
    if request.POST and 'jobPostUpdate' in request.POST:
        jobpost_form = JobPostForm(request.POST, instance=jobpost)
        if jobpost_form.is_valid():
            jobpost_form.save()
            return redirect('manager:home')
    context = {
        "jobpost": jobpost,
        "jobpost_form": jobpost_form
    }
    return render(request, "manager/update_job_post.html", context)


@login_required
@manager_required
def delete_job_post(request, jobpost_uuid):
    jobpost = JobPost.objects.get_with_uuid(jobpost_uuid, request.user)
    if jobpost is None:
        return HttpResponseNotFound()
    jobpost.activity_status = ActivityStatusTypeEnum.passive.value
    jobpost.deleted_at = timezone.now()
    jobpost.save()
    return redirect('manager:home')


@login_required
@manager_required
def detail_job_post(request, jobpost_uuid):
    jobpost = JobPost.objects.get_with_uuid(jobpost_uuid, request.user)
    if jobpost is None:
        return HttpResponseNotFound()
    context = {
        "jobpost": jobpost,
        "candidate_list": JobApplication.objects.get_candidate_list(jobpost)
    }
    return render(request, "manager/detail_job_post.html", context)


@login_required
@manager_required
def detail_job_application(request, jobapplication_uuid):
    job_application = JobApplication.objects.get_with_uuid(jobapplication_uuid, request.user)
    if job_application is None:
        return HttpResponseNotFound()
    job_application_form = JobApplicationDetailForm(instance=job_application)
    if request.POST and 'jobApplicationUpdate' in request.POST:
        job_application_form = JobApplicationDetailForm(request.POST, instance=job_application)
        if job_application_form.is_valid():
            job_application_form.save()
            return redirect('manager:detail-job-post', job_application.job_post.uuid)
    context = {
        "job_application": job_application,
        "job_application_form": job_application_form
    }
    return render(request, "manager/detail_job_application.html", context)
