from django.urls import path

from . import views

app_name = "football"
urlpatterns = [
    path("", views.GameListView.as_view(), name="gamelist"),
    # path("league/", views.GameListView.as_view(), name="gamelist"),
    path(
        "league/<int:league_pk>/",
        views.GameLeagueListView.as_view(),
        name="gamelist-by-league",
    ),
    path("edit/<int:pk>/", views.GameUpdateFoulInformation, name="update-game"),
    path("<int:pk>/", views.GameDetailView.as_view(), name="view-game"),
]
