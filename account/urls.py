from django.urls import path

from account.views import login, register, logout

app_name = "account"

urlpatterns = [
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('register', register, name="register"),
]
