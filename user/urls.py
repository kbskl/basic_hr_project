from django.urls import path
from . import views
from .views import profile

app_name = "user"

urlpatterns = [
    path('profile', profile, name="profile"),
]
