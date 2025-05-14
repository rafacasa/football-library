from django.urls import path

from . import views

app_name = "football"
urlpatterns = [
    path("", views.GameListView.as_view(), name="gamelist"),
    path("edit/<int:pk>/", views.GameUpdateFoulInformation, name="update-game"),
    path("<int:pk>/", views.GameDetailView.as_view(), name="view-game"),
]
