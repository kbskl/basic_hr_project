from enum import Enum


class GeneralEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.value, i.value) for i in cls)

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class JobApplicationStatusEnum(GeneralEnum):
    reject = "Red edildi"
    accept = "Kabul edildi"
    under_review = "İnceleniyor"
    delivered = "Gönderildi"


class ActivityStatusTypeEnum(GeneralEnum):
    active = 'Active'
    passive = 'Passive'


class GenderEnum(GeneralEnum):
    male = 'Erkek'
    female = 'Kadın'


class ProfileStatusEnum(GeneralEnum):
    jobseeker = "İş Arayan"
    employer = "İş Veren"


class JobStatusEnum(GeneralEnum):
    completed = "Tamamlandı"
    canceled = "Pasif"
    pending = "Aktif"


class JobApplicationEnum(GeneralEnum):
    approved = "Onaylandı"
    denied = "Reddedildi"
    under_review = "İnceleniyor"
    pending = "Bekleniyor"


class WorkingModelEnum(GeneralEnum):
    remote = "Uzaktan"
    hybrid = "Hybrid"
    in_place = "Yerinde"
