from django.http import HttpResponseNotFound

from general.utility.enums import ProfileStatusEnum


def jobseek_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.profile.profile_status == ProfileStatusEnum.jobseeker.value:
            return function(request, *args, **kwargs)
        return HttpResponseNotFound()

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def manager_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.profile.profile_status == ProfileStatusEnum.employer.value:
            return function(request, *args, **kwargs)
        return HttpResponseNotFound()

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
