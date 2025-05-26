import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    team_name = models.CharField(
        max_length=100,
        verbose_name=_("team name"),
    )

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = _("team")
        verbose_name_plural = _("teams")


class League(models.Model):
    slug = models.SlugField(blank=True, unique=True)
    name = models.CharField(
        max_length=100,
        verbose_name=_("league name"),
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("league")
        verbose_name_plural = _("leagues")


class Season(models.Model):
    slug = models.SlugField(blank=True, unique=True)
    season_name = models.CharField(
        max_length=50,
        verbose_name=_("season name"),
    )

    def __str__(self):
        return self.season_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.season_name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("season")
        verbose_name_plural = _("seasons")


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        verbose_name=_("home team"),
        related_name="home_game_set",
    )
    home_team_score = models.PositiveIntegerField(
        blank=True,
        default=0,
        verbose_name=_("home team score"),
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        verbose_name=_("away team"),
        related_name="away_game_set",
    )
    away_team_score = models.PositiveIntegerField(
        blank=True,
        default=0,
        verbose_name=_("away team score"),
    )
    date = models.DateTimeField(
        verbose_name=_("game time"),
        blank=True,
        null=True,
    )
    video_link = models.URLField(
        verbose_name=_("link to game's videos"),
        blank=True,
    )
    league = models.ForeignKey(
        League,
        on_delete=models.PROTECT,
        verbose_name=_("league"),
    )
    fouls_in_game = models.ManyToManyField(
        "Foul",
        through="Game_Foul",
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.PROTECT,
        verbose_name=_("season"),
    )

    def is_past_game(self):
        diff = timezone.now() - self.date
        return diff >= timezone.timedelta(seconds=1)

    def get_absolute_url(self):
        return reverse("football:view-game", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"

    class Meta:
        verbose_name = _("game")
        verbose_name_plural = _("games")


class Foul(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("foul name"),
    )
    short_name = models.CharField(
        max_length=5,
        verbose_name=_("foul short name"),
    )
    enabled = models.BooleanField(
        default=False,
        verbose_name=_("enabled"),
    )

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _("foul")
        verbose_name_plural = _("fouls")


class Game_Foul(models.Model):
    class Period(models.TextChoices):
        QTR1 = "1 QTR", _("First Quarter")
        QTR2 = "2 QTR", _("Second Quarter")
        QTR3 = "3 QTR", _("Third Quarter")
        QTR4 = "4 QTR", _("Fourth Quarter")
        OT = "OT", _("Overtime")

    game = models.ForeignKey(
        Game,
        on_delete=models.PROTECT,
        verbose_name=_("game"),
    )
    foul = models.ForeignKey(
        Foul,
        on_delete=models.PROTECT,
        verbose_name=_("foul"),
    )
    period = models.CharField(
        max_length=5,
        choices=Period,
        default=Period.QTR1,
        verbose_name=_("period"),
    )

    class Meta:
        verbose_name = _("game foul")
        verbose_name_plural = _("game fouls")
