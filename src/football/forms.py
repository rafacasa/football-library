from django.forms import ModelForm, inlineformset_factory

from .models import Game, Game_Foul


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["home_team_score", "away_team_score", "video_link"]


GameFoulFormSet = inlineformset_factory(
    Game,
    Game_Foul,
    fields=["foul", "period"],
    extra=1,
)
