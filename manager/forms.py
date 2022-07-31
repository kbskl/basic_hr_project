from django import forms
from core.models import JobPost, JobApplication
from general.utility.enums import JobApplicationEnum


class JobPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance', None) is None:
            self.fields['job_post_status'].widget = forms.HiddenInput()
        self.fields['job_description'].required = True
        self.fields['working_model'].required = True
        self.fields['job_required'].required = True
        self.fields['location'].required = True

    class Meta:
        model = JobPost
        fields = ('job', 'job_post_status', 'job_description', 'job_required', 'working_model', 'location')


class JobApplicationDetailForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('employer_note', 'job_application_status')
