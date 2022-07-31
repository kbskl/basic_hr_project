from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import JobPost, JobApplication
from general.utility.decorators import jobseek_required
from jobseek.forms import JobApplicationApplyForm
from jobseek.utility.filterset import JobPostFilter


@login_required
@jobseek_required
def home(request):
    special_posts = JobPost.objects.get_posts_for_user(request.user)
    context = {
        "all_posts": special_posts
    }
    return render(request, "jobseek/home.html", context)


@login_required
@jobseek_required
def detail_job_post(request, jobpost_uuid):
    jobpost = JobPost.objects.get_with_uuid_for_jobseeker(jobpost_uuid)
    if jobpost is None:
        return HttpResponseNotFound()
    context = {
        "jobpost": jobpost,
        "jobapplication_form": JobApplicationApplyForm(),
        "jobapplication": JobApplication.objects.get_with_jobseeker_and_jobpost(jobpost, request.user)
    }
    return render(request, "jobseek/detail_job_post.html", context)


@login_required
@jobseek_required
def apply_job_post(request, jobpost_uuid):
    jobpost = JobPost.objects.get_with_uuid_for_jobseeker(jobpost_uuid)
    if jobpost is None:
        return HttpResponseNotFound()
    if request.POST and 'jobApplicationSubmit' in request.POST:
        jobapplication_form = JobApplicationApplyForm(request.POST)
        if jobapplication_form.is_valid():
            jobapplication = jobapplication_form.save(commit=False)
            jobapplication.jobseeker = request.user
            jobapplication.job_post = jobpost
            jobapplication.save()
    return redirect('jobseek:home')


@login_required
@jobseek_required
def fast_apply_job_post(request, jobpost_uuid):
    jobpost = JobPost.objects.get_with_uuid_for_jobseeker(jobpost_uuid)
    if jobpost is None:
        return HttpResponseNotFound()
    JobApplication.objects.create(jobseeker=request.user, job_post=jobpost)
    return redirect('jobseek:home')


@login_required
@jobseek_required
def my_job_application(request):
    all_applications = JobApplication.objects.get_all(request.user)
    context = {
        "all_applications": all_applications
    }
    return render(request, "jobseek/my_job_application.html", context)


@login_required
@jobseek_required
def all_job_post(request):
    posts = JobPost.objects.get_all_posts_for_user(request.user)
    all_posts = JobPostFilter(request.GET, queryset=posts)
    context = {
        "all_posts": all_posts
    }
    return render(request, "jobseek/all_job_posts.html", context)
