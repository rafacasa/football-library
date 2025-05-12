from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .forms import GameForm, GameFoulFormSet, GameFoulFormSetHelper
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
    template_name = "football/game_update.html"
    form_class = GameForm
    formset_class = GameFoulFormSet
    formset_helper_class = GameFoulFormSetHelper

    def get_formset_class(self):
        if self.formset_class:
            return self.formset_class
        raise ImproperlyConfigured("Specifying 'formset_class' is required")

    def get_formset_kwargs(self):
        return self.get_form_kwargs()

    def get_formset(self, formset_class=None):
        if formset_class is None:
            formset_class = self.get_formset_class()
        return formset_class(**self.get_formset_kwargs())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "formset" not in context:
            context["formset"] = self.get_formset()
            context["formset_helper"] = GameFoulFormSetHelper()
        return context

    def form_valid(self, form, formset):
        formset.save()
        return super().form_valid(form)

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        formset = self.get_formset()

        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)


def add_foul_on_formset(request, pk):
    game = get_object_or_404(Game, pk=pk)
    form = GameForm(request.POST, instance=game)
    formset = GameFoulFormSet(request.POST, instance=game)
    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        # formset2 = GameFoulFormSet(instance=game)
        # return render parcial do form e formset2
