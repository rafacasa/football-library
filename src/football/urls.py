from django.urls import path

from . import views

app_name = "football"
urlpatterns = [
    path("", views.GameListView.as_view(), name="gamelist"),
    # path("league/", views.GameListView.as_view(), name="gamelist"),
    path(
        "league/<slug:league_slug>/",
        views.GameLeagueListView.as_view(),
        name="gamelist-by-league",
    ),
    path("edit/<uuid:pk>/", views.GameUpdateFoulInformation, name="update-game"),
    path("<uuid:pk>/", views.GameDetailView.as_view(), name="view-game"),
]
