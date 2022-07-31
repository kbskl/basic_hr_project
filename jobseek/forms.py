from django import forms

from core.models import JobApplication


class JobApplicationApplyForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('jobseeker_note',)
