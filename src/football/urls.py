from django.urls import path

from . import views

app_name = "football"
urlpatterns = [
    path("", views.GameListView.as_view(), name="gamelist"),
    path("league/", views.LeagueListView.as_view(), name="leaguelist"),
    path(
        "league/<slug:league_slug>/",
        views.GameLeagueListView.as_view(),
        name="gamelist-by-league",
    ),
    path(
        "league/<slug:league_slug>/<slug:season_slug>",
        views.GameLeagueSeasonListView.as_view(),
        name="gamelist-by-league-and-season",
    ),
    path("edit/<uuid:pk>/", views.GameUpdateFoulInformation, name="update-game"),
    path("<uuid:pk>/", views.GameDetailView.as_view(), name="view-game"),
]
