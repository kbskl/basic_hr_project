import uuid

from django.contrib.auth.models import User
from django.db import models

from core.utility.model_managers import JobPostModelManager, JobApplicationModelManager
from general.utility.enums import JobApplicationEnum, JobStatusEnum, WorkingModelEnum, ActivityStatusTypeEnum
from general.utility.models import GeneralModel


class Province(GeneralModel):
    name = models.CharField(max_length=255, verbose_name="Şehir")

    def __str__(self):
        return self.name


class JobPost(GeneralModel):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="İş Veren")
    job = models.CharField(max_length=255, verbose_name="Pozisyon")
    job_description = models.TextField(verbose_name="İş Tanımı", blank=True, null=True)
    job_required = models.TextField(verbose_name="Aranan Nitelikler", blank=True, null=True)
    job_post_status = models.CharField(choices=JobStatusEnum.choices(), default=JobStatusEnum.pending.value, verbose_name='İş Durumu', blank=True, null=True, max_length=50)
    working_model = models.CharField(choices=WorkingModelEnum.choices(), verbose_name='Çalışma Modeli', blank=True, null=True, max_length=50)
    location = models.ForeignKey(Province, on_delete=models.SET_NULL, verbose_name='Konum', blank=True, null=True, max_length=50)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    objects = JobPostModelManager()

    @property
    def job_application_count(self):
        return JobApplication.objects.filter(job_post=self, activity_status=ActivityStatusTypeEnum.active.value).count()

    def save(self, *args, **kwargs):
        if self.uuid is None:
            self.uuid = uuid.uuid4()
        super(JobPost, self).save(*args, **kwargs)


class JobApplication(GeneralModel):
    jobseeker = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="İşe Başvuran", related_name="tojobapplications")
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE, blank=True, null=True, verbose_name="İş İlanı")
    jobseeker_note = models.TextField(blank=True, null=True, verbose_name="Başvuru Notu")
    employer_note = models.TextField(blank=True, null=True, verbose_name="İnceleme Notu")
    job_application_status = models.CharField(choices=JobApplicationEnum.choices(), default=JobApplicationEnum.pending.value, verbose_name='Başvuru Durumu', blank=True, null=True, max_length=60)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    objects = JobApplicationModelManager()

    def save(self, *args, **kwargs):
        if self.uuid is None:
            self.uuid = uuid.uuid4()
        super(JobApplication, self).save(*args, **kwargs)
