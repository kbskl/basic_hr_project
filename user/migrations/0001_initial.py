# Generated by Django 4.0.6 on 2022-07-29 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.utility.upload_paths


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('activity_status', models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive')], default='Active', max_length=50, verbose_name='Aktiflik Durumu')),
                ('birth_day', models.DateTimeField(blank=True, null=True, verbose_name='Doğum Tarihi')),
                ('gender', models.CharField(blank=True, choices=[('Erkek', 'Erkek'), ('Kadın', 'Kadın')], max_length=20, null=True, verbose_name='Cinsiyet')),
                ('profile_status', models.CharField(blank=True, choices=[('İş Arayan', 'İş Arayan'), ('İş Veren', 'İş Veren')], max_length=20, null=True, verbose_name='Profil Durumu')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CareerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('activity_status', models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive')], default='Active', max_length=50, verbose_name='Aktiflik Durumu')),
                ('cv', models.FileField(blank=True, null=True, upload_to=user.utility.upload_paths.get_cv_upload_file_path, verbose_name='CV')),
                ('targeted_jobs', models.ManyToManyField(blank=True, related_name='jobcareerprofile', to='core.job')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
