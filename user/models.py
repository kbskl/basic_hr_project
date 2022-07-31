from django.contrib.auth.models import User
from django.db import models

from core.models import Province
from general.utility.enums import GenderEnum, ProfileStatusEnum, WorkingModelEnum
from general.utility.models import GeneralModel
from user.utility.upload_paths import get_cv_upload_file_path


class Profile(GeneralModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day = models.DateTimeField(blank=True, null=True, verbose_name="Doğum Tarihi")
    gender = models.CharField(choices=GenderEnum.choices(), verbose_name='Cinsiyet', blank=True, null=True, max_length=20)
    profile_status = models.CharField(choices=ProfileStatusEnum.choices(), verbose_name='Profil Durumu', blank=True, null=True, max_length=20)

    def __str__(self):
        return self.user.username


class CareerProfile(GeneralModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv = models.FileField(upload_to=get_cv_upload_file_path, blank=True, null=True, verbose_name="CV")
    job = models.CharField(max_length=255, verbose_name="Pozisyon", blank=True, null=True)
    working_model = models.CharField(choices=WorkingModelEnum.choices(), verbose_name='Çalışma Modeli', blank=True, null=True, max_length=50)
    location = models.ForeignKey(Province, on_delete=models.SET_NULL, verbose_name='Konum', blank=True, null=True, max_length=50)

    def __str__(self):
        return self.user.username
