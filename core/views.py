from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from general.utility.enums import ProfileStatusEnum


@login_required
def home(request):
    if request.user.profile.profile_status == ProfileStatusEnum.jobseeker.value:
        return redirect('jobseek:home')
    elif request.user.profile.profile_status == ProfileStatusEnum.employer.value:
        return redirect('manager:home')
    return HttpResponseNotFound()
