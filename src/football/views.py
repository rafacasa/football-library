from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .forms import GameForm, GameFoulFormSet, GameFoulFormSetHelper
from .models import Game, Game_Foul, League, Season


class LeagueListView(ListView):
    model = League
    context_object_name = "leagues"
    template_name = "football/leagues_list.html"


class GameListView(ListView):
    model = Game
    context_object_name = "games"
    template_name = "football/games_list.html"


class GameLeagueListView(GameListView):
    def get_queryset(self):
        self.league = get_object_or_404(League, slug=self.kwargs["league_slug"])
        return Game.objects.filter(league=self.league)


# TODO Criar o template apenas da tabela de jogos e criar um template para cada visao
# TODO Colocar um cabeçalho para cada visao de jogos
class GameLeagueSeasonListView(GameListView):
    def get_queryset(self):
        self.league = get_object_or_404(League, slug=self.kwargs["league_slug"])
        self.season = get_object_or_404(Season, slug=self.kwargs["season_slug"])
        return Game.objects.filter(league=self.league, season=self.season)


class GameDetailView(DetailView):
    model = Game
    template_name = "football/game_view.html"
    context_object_name = "game"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_fouls = Game_Foul.objects.filter(game=self.get_object())
        context["game_fouls"] = game_fouls
        return context


def GameUpdateFoulInformation(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        formset = GameFoulFormSet(request.POST, instance=game)

        if form.is_valid() and formset.is_valid():
            # TODO save all information on a transaction
            form.save()
            formset.save()
            return redirect("football:view-game", pk=pk)
    else:
        form = GameForm(instance=game)
        formset = GameFoulFormSet(instance=game)

    context = {
        "form": form,
        "game": game,
        "formset": formset,
        "formset_helper": GameFoulFormSetHelper(),
    }

    return render(request, "football/game_update.html", context)
