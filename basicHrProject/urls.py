"""basicHrProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.forms import UserPasswordResetForm, UserPasswordResetConfirmForm

urlpatterns = [
                  path('', include('core.urls')),
                  path('account/', include('account.urls')),
                  path('jobseek/', include('jobseek.urls')),
                  path('manager/', include('manager.urls')),
                  path('user/', include('user.urls')),
                  path('admin/', admin.site.urls),
                  path('password_reset/', auth_views.PasswordResetView.as_view(
                      html_email_template_name='registration/password_reset_email.html',
                      form_class=UserPasswordResetForm), name="password_reset"),
                  path('reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(form_class=UserPasswordResetConfirmForm),
                       name='password_reset_confirm'),
                  path('', include('django.contrib.auth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
