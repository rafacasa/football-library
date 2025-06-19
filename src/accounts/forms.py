from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit
from django.contrib.auth.forms import (
    AdminUserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from django.forms.fields import CharField
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")


class AccountsAuthForm(AuthenticationForm):
    next_page = CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            FloatingField("username", wrapper_class="mb-md-4"),
            FloatingField("password", wrapper_class="mb-md-4"),
            Field("next_page", type="hidden"),
            Div(
                Submit("login", _("Login"), wrapper_class=""),
                css_class="d-grid",
            ),
        )
