from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm, inlineformset_factory

from .models import Game, Game_Foul


class GameForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-2"
        self.helper.field_class = "col-lg-6"

    class Meta:
        model = Game
        fields = ["home_team_score", "away_team_score", "video_link"]


GameFoulFormSet = inlineformset_factory(
    Game,
    Game_Foul,
    fields=["foul", "period"],
    extra=1,
)


class GameFoulFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_tag = False
        self.disable_csrf = True
        self.add_input(Submit("submit", "Update"))
        self.template = "bootstrap5/table_inline_formset.html"
        # self.field_class = "col-lg-3"
