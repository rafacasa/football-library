from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Team(models.Model):
    team_name = models.CharField(
        max_length=100,
        verbose_name="team name",
        help_text="Enter the Team name:",  # TODO Translations
    )

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = "team"  # TODO Translations
        verbose_name_plural = "teams"  # TODO Translations


class League(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="league name",
        help_text="Enter the League name:",  # TODO Translations
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "league"  # TODO Translations
        verbose_name_plural = "leagues"  # TODO Translations


class Season(models.Model):
    season_name = models.CharField(
        max_length=50,
        verbose_name="season name",  # TODO Translations
        help_text="Enter the Season name: ",  # TODO Translations
    )

    def __str__(self):
        return self.season_name

    class Meta:
        verbose_name = "season"  # TODO Translations
        verbose_name_plural = "seasons"  # TODO Translations


class Game(models.Model):
    home_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        verbose_name="home team",
        help_text="Select the home Team:",  # TODO Translations
        related_name="home_game_set",
    )
    home_team_score = models.PositiveIntegerField(blank=True, default=0)
    away_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        verbose_name="away team",
        help_text="Select the away Team:",  # TODO Translations
        related_name="away_game_set",
    )
    away_team_score = models.PositiveIntegerField(blank=True, default=0)
    date = models.DateTimeField(
        verbose_name="game time",
        help_text="Select the game time:",  # TODO Translations
        blank=True,
    )
    video_link = models.URLField(
        verbose_name="link to game's videos",
        help_text="Enter the link for the game's video:",  # TODO Translations
        blank=True,
    )
    league = models.ForeignKey(
        League,
        on_delete=models.PROTECT,
        verbose_name="league",
        help_text="Enter this game's league:",  # TODO Translations
    )
    fouls_in_game = models.ManyToManyField(
        "Foul",
        through="Game_Foul",
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.PROTECT,
        verbose_name="season",  # TODO Translations
        help_text="Select the game season",  # TODO Translations
    )

    def is_past_game(self):
        diff = timezone.now() - self.date
        return diff >= timezone.timedelta(seconds=1)

    def get_absolute_url(self):
        return reverse("football:view-game", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

    class Meta:
        verbose_name = "game"  # TODO Translations
        verbose_name_plural = "games"  # TODO Translations


class Foul(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="foul name",
        help_text="Enter the Foul name:",
    )  # TODO Translations
    short_name = models.CharField(
        max_length=5,
        verbose_name="foul short name",
        help_text="Enter the Foul short name:",
    )  # TODO Translations

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "foul"  # TODO Translations
        verbose_name_plural = "fouls"  # TODO Translations


class Game_Foul(models.Model):
    class Period(models.TextChoices):
        QTR1 = "1 QTR", "First Quarter"
        QTR2 = "2 QTR", "Second Quarter"
        QTR3 = "3 QTR", "Third Quarter"
        QTR4 = "4 QTR", "Fourth Quarter"
        OT = "OT", "Overtime"  # TODO Translations

    game = models.ForeignKey(
        Game,
        on_delete=models.PROTECT,
        verbose_name="game",
        help_text="Enter the game where the foul happend:",  # TODO Translations
    )
    foul = models.ForeignKey(
        Foul,
        on_delete=models.PROTECT,
        verbose_name="foul",
        help_text="Enter the foul:",  # TODO Translations
    )
    period = models.CharField(
        max_length=5,
        choices=Period,
        default=Period.QTR1,
        verbose_name="period",
        help_text="Enter the period when the foul happend:",  # TODO Translations
    )

    class Meta:
        verbose_name = "game foul"  # TODO Translations
        verbose_name_plural = "game fouls"  # TODO Translations
