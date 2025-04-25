import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Game, League, Season, Team


class GameModelTeste(TestCase):
    def _create_test_season(self, name="test"):
        return Season.objects.create(season_name=name)

    def _create_test_league(self, name="test"):
        return League.objects.create(name=name)

    def _create_test_team(self, name="test"):
        return Team.objects.create(team_name=name)

    def _create_game_with_timedelta(self, days=0, hours=0, minutes=0, seconds=0):
        time = timezone.now() + datetime.timedelta(
            days=days, hours=hours, minutes=minutes, seconds=seconds
        )
        season = self._create_test_season()
        league = self._create_test_league()
        team1 = self._create_test_team(name="team1")
        team2 = self._create_test_team(name="team2")
        return Game.objects.create(
            date=time,
            home_team=team1,
            away_team=team2,
            league=league,
            season=season,
        )

    def test_past_game_with_future_date_by_days(self):
        game_test = self._create_game_with_timedelta(days=2)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_future_date_by_hours(self):
        game_test = self._create_game_with_timedelta(hours=2)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_future_date_by_minutes(self):
        game_test = self._create_game_with_timedelta(minutes=1)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_future_date_by_seconds(self):
        game_test = self._create_game_with_timedelta(seconds=2)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_same_date(self):
        game_test = self._create_game_with_timedelta()
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_past_date_by_days(self):
        game_test = self._create_game_with_timedelta(days=-2)
        self.assertIs(game_test.is_past_game(), True)

    def test_past_game_with_past_date_by_minutes(self):
        game_test = self._create_game_with_timedelta(minutes=-1)
        self.assertIs(game_test.is_past_game(), True)

    def test_past_game_with_past_date_by_hours(self):
        game_test = self._create_game_with_timedelta(hours=-2)
        self.assertIs(game_test.is_past_game(), True)

    def test_past_game_with_past_date_by_seconds(self):
        game_test = self._create_game_with_timedelta(seconds=-2)
        self.assertIs(game_test.is_past_game(), True)
