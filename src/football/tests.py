import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Foul, Game, League, Season, Team


def _create_test_season(name="test"):
    return Season.objects.create(season_name=name)


def _create_test_league(name="test"):
    return League.objects.create(name=name)


def _create_test_team(name="test"):
    return Team.objects.create(team_name=name)


def _create_game(season="test", league="test", team1="team1", team2="team2", save=True):
    season = _create_test_season(name=season)
    league = _create_test_league(name=league)
    team1 = _create_test_team(name=team1)
    team2 = _create_test_team(name=team2)
    game = Game(
        home_team=team1,
        away_team=team2,
        league=league,
        season=season,
    )
    if save:
        game.save()
    return game


def _create_game_with_timedelta(
    days=0,
    hours=0,
    minutes=0,
    seconds=0,
    season="test",
    league="test",
    team1="team1",
    team2="team2",
    save=True,
):
    game = _create_game(
        season=season, league=league, team1=team1, team2=team2, save=False
    )
    time = timezone.now() + datetime.timedelta(
        days=days, hours=hours, minutes=minutes, seconds=seconds
    )
    game.date = time
    if save:
        game.save()
    return game


class GameModelTeste(TestCase):

    def test_past_game_with_future_date_by_days(self):
        game_test = _create_game_with_timedelta(days=2)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_future_date_by_hours(self):
        game_test = _create_game_with_timedelta(hours=2)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_future_date_by_minutes(self):
        game_test = _create_game_with_timedelta(minutes=1)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_future_date_by_seconds(self):
        game_test = _create_game_with_timedelta(seconds=2)
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_same_date(self):
        game_test = _create_game_with_timedelta()
        self.assertIs(game_test.is_past_game(), False)

    def test_past_game_with_past_date_by_days(self):
        game_test = _create_game_with_timedelta(days=-2)
        self.assertIs(game_test.is_past_game(), True)

    def test_past_game_with_past_date_by_minutes(self):
        game_test = _create_game_with_timedelta(minutes=-1)
        self.assertIs(game_test.is_past_game(), True)

    def test_past_game_with_past_date_by_hours(self):
        game_test = _create_game_with_timedelta(hours=-2)
        self.assertIs(game_test.is_past_game(), True)

    def test_past_game_with_past_date_by_seconds(self):
        game_test = _create_game_with_timedelta(seconds=-2)
        self.assertIs(game_test.is_past_game(), True)

    def test_get_relative_url_page_render(self):
        game_test = _create_game()
        path = game_test.get_absolute_url()
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["game"], game_test)

    def test_str_conversion(self):
        game_test = _create_game(team1="Time 1", team2="Time 2")
        self.assertEqual(str(game_test), "Time 1 vs Time 2")


class TeamModelTeste(TestCase):
    def test_str_conversion(self):
        team_test = _create_test_team("Time 1")
        self.assertEqual(str(team_test), "Time 1")


class LeagueModelTeste(TestCase):
    def test_str_conversion(self):
        league_test = _create_test_league("Liga Teste")
        self.assertEqual(str(league_test), "Liga Teste")

    def test_save_create_slug(self):
        league_test = _create_test_league("Campeonato Brasileiro")
        self.assertEqual(league_test.slug, "campeonato-brasileiro")

    def test_edit_existing_league_updates_slug(self):
        league_test = _create_test_league("Campeonato Brasileiro")
        league_test.name = "Novo Nome Trocado"
        league_test.save()
        self.assertEqual(league_test.slug, "novo-nome-trocado")


class SeasonModelTeste(TestCase):
    def test_str_conversion(self):
        season_test = _create_test_season("Test Season")
        self.assertEqual(str(season_test), "Test Season")

    def test_save_create_slug_only_numbers(self):
        season_test = _create_test_season("2025")
        self.assertEqual(season_test.slug, "2025")

    def test_save_create_slug(self):
        season_test = _create_test_season("Temporada Atual 2025")
        self.assertEqual(season_test.slug, "temporada-atual-2025")

    def test_edit_existing_league_updates_slug(self):
        season_test = _create_test_season("Temporada Atual 2023")
        season_test.season_name = "Nome Trocado Temporada 2025"
        season_test.save()
        self.assertEqual(season_test.slug, "nome-trocado-temporada-2025")


class FoulModelTeste(TestCase):
    def test_str_conversion(self):
        foul_test = Foul.objects.create(
            name="False Start", short_name="FST", enabled=True
        )
        self.assertEqual(str(foul_test), "FST - False Start")
