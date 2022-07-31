from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from account.forms import UserPasswordChangeForm
from general.utility.enums import ProfileStatusEnum
from user.forms import UserForm, CareerProfileForm


@login_required
def profile(request):
    user_form = UserForm(instance=request.user)
    password_form = UserPasswordChangeForm(user=request.user)
    if request.POST and 'updateUserManagerProfile' in request.POST:
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:profile')
    if request.POST and 'updatePassword' in request.POST:
        password_form = UserPasswordChangeForm(data=request.POST, user=request.user)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, request.user)
            return redirect('user:profile')
    if request.POST and 'updateKariyerProfile' in request.POST:
        career_profile_form = CareerProfileForm(request.POST, request.FILES, instance=request.user.careerprofile)
        if career_profile_form.is_valid():
            career_profile_form.save()
            return redirect('user:profile')
    context = {
        "user_form": user_form,
        "password_form": password_form
    }
    if request.user.profile.profile_status == ProfileStatusEnum.employer.value:
        html_temp = "user/manager/profile.html"
    else:

        html_temp = "user/jobseek/profile.html"
        context['career_profile_form'] = CareerProfileForm(instance=request.user.careerprofile)
    return render(request, html_temp, context)
