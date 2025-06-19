from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("logout/", views.AccountLogoutView.as_view(), name="logout"),
    path("login/", views.AccountLoginView.as_view(), name="login"),
]
