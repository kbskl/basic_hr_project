from django.db import models
from django.db.models import Q

from general.utility.enums import ActivityStatusTypeEnum, JobStatusEnum


class JobPostModelManager(models.Manager):

    def get_all(self, user):
        q1 = Q(employer=user)
        q2 = Q(activity_status=ActivityStatusTypeEnum.active.value)
        return super().get_queryset().filter(q1 & q2).order_by('-created_at')

    def get_with_uuid(self, uuid, user):
        q1 = Q(employer=user)
        q2 = Q(activity_status=ActivityStatusTypeEnum.active.value)
        q3 = Q(uuid=uuid)
        return super().get_queryset().filter(q1 & q2 & q3).first()

    def get_with_uuid_for_jobseeker(self, uuid):
        q1 = Q(job_post_status=JobStatusEnum.pending.value)
        q2 = Q(activity_status=ActivityStatusTypeEnum.active.value)
        q3 = Q(uuid=uuid)
        return super().get_queryset().filter(q1 & q2 & q3).first()

    def get_all_posts_for_user(self, user):
        q_objects = Q()
        q_objects &= Q(activity_status=ActivityStatusTypeEnum.active.value)
        q_objects &= Q(job_post_status=JobStatusEnum.pending.value)
        return super().get_queryset().exclude(pk__in=user.tojobapplications.all().values_list("job_post__pk", flat=True)).filter(q_objects).order_by('-created_at')

    def get_posts_for_user(self, user):
        q_objects = Q()
        q_objects &= Q(activity_status=ActivityStatusTypeEnum.active.value)
        q_objects &= Q(job_post_status=JobStatusEnum.pending.value)
        if user.careerprofile.job:
            q_objects &= Q(job__icontains=user.careerprofile.job)
        if user.careerprofile.location:
            q_objects &= Q(location=user.careerprofile.location)
        if user.careerprofile.working_model:
            q_objects &= Q(working_model=user.careerprofile.working_model)
        return super().get_queryset().exclude(pk__in=user.tojobapplications.all().values_list("job_post__pk", flat=True)).filter(q_objects).order_by('-created_at')


class JobApplicationModelManager(models.Manager):

    def get_candidate_list(self, jobpost):
        q1 = Q(job_post=jobpost)
        q2 = Q(activity_status=ActivityStatusTypeEnum.active.value)
        q3 = Q(job_post__activity_status=ActivityStatusTypeEnum.active.value)
        return super().get_queryset().filter(q1 & q2 & q3).order_by('-created_at')

    def get_with_uuid(self, uuid, user):
        q1 = Q(job_post__employer=user)
        q2 = Q(activity_status=ActivityStatusTypeEnum.active.value)
        q3 = Q(uuid=uuid)
        q4 = Q(job_post__activity_status=ActivityStatusTypeEnum.active.value)
        return super().get_queryset().filter(q1 & q2 & q3 & q4).first()

    def get_all(self, user):
        q1 = Q(jobseeker=user)
        q2 = Q(activity_status=ActivityStatusTypeEnum.active.value)
        q3 = Q(job_post__activity_status=ActivityStatusTypeEnum.active.value)
        return super().get_queryset().filter(q1 & q2 & q3).order_by('-created_at')

    def get_with_jobseeker_and_jobpost(self, jobpost, user):
        q1 = Q(jobseeker=user)
        q2 = Q(activity_status=ActivityStatusTypeEnum.active.value)
        q3 = Q(job_post=jobpost)
        q4 = Q(job_post__activity_status=ActivityStatusTypeEnum.active.value)
        return super().get_queryset().filter(q1 & q2 & q3 & q4).first()
