from django.forms import ModelForm

from .models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["home_team_score", "away_team_score", "video_link"]
