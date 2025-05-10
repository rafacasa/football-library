from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .forms import GameForm
from .models import Game, Game_Foul


class GameListView(ListView):
    model = Game
    context_object_name = "games"
    template_name = "football/games_list.html"


class GameDetailView(DetailView):
    model = Game
    template_name = "football/game_view.html"
    context_object_name = "game"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_fouls = Game_Foul.objects.filter(game=self.get_object())
        context["game_fouls"] = game_fouls
        return context


class GameUpdateView(UpdateView):
    model = Game
    template_name = "football/update_game.html"
    form_class = GameForm
