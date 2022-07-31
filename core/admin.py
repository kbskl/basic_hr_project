from django.contrib import admin

from core.models import JobPost, JobApplication, Province

admin.site.register(JobPost)
admin.site.register(JobApplication)
admin.site.register(Province)
