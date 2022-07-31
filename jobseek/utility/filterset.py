import django_filters
from core.models import JobPost, Province
from general.utility.enums import ActivityStatusTypeEnum, WorkingModelEnum


class JobPostFilter(django_filters.FilterSet):
    created_at = django_filters.DateRangeFilter(label='Oluşturulma Aralığı')
    job = django_filters.CharFilter(lookup_expr='icontains', label='Pozisyon')
    job_description = django_filters.CharFilter(lookup_expr='icontains', label='İş Tanımı')
    job_required = django_filters.CharFilter(lookup_expr='icontains', label='Aranan Nitelikler')
    location = django_filters.ModelChoiceFilter(queryset=Province.objects.filter(activity_status=ActivityStatusTypeEnum.active.value), label='Konum')
    working_model = django_filters.ChoiceFilter(label="Çalışma Modeli", choices=WorkingModelEnum.choices())

    class Meta:
        model = JobPost
        fields = ['created_at', 'job', 'job_description', 'job_required', 'working_model', 'location']
