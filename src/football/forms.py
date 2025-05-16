from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Div, Layout, Row
from django.forms import ModelForm, inlineformset_factory

from .models import Game, Game_Foul


class GameForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-3"
        self.helper.field_class = "col-lg-9"
        self.helper.layout = Layout(
            Row(
                Div("home_team_score", css_class="col"),
                Div("away_team_score", css_class="col"),
            ),
            Row(
                Div("video_link", css_class="col"),
            ),
        )
        if self.instance is not None:
            self.fields["home_team_score"].label = f"Placar {self.instance.home_team}"
            self.fields["away_team_score"].label = f"Placar {self.instance.away_team}"

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
        self.form_class = "form-horizontal"
        self.label_class = "col-lg-2"
        self.field_class = "col-lg-10"
        self.layout = Layout(
            Div(
                Div("foul", css_class="col"),
                Div("period", css_class="col"),
                Div(
                    HTML(
                        '<button class="btn btn-outline-danger" id="id_button_'
                        'delete_set-{{forloop.counter|add:"-1" }}"><i class="bi '
                        'bi-trash"></i></button>'
                    ),
                    # StrictButton(
                    #     '<i class="bi bi-trash"></i>',
                    #     "id_button_delete_set-{{forloop.counter}}",
                    #     css_class="btn btn-outline-danger",
                    # ),
                    css_class="col-auto text-end",
                ),
                css_class="row",
            )
        )
