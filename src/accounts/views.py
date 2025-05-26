from django.contrib.auth.views import LoginView, LogoutView

from .forms import AccountsAuthForm


class AccountLogoutView(LogoutView):
    redirect_field_name = "next"
    next_page = "football:gamelist"


class AccountLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_field_name = "next_page"
    next_page = "football:gamelist"
    authentication_form = AccountsAuthForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context["next_page"]:
            context["form"].initial["next_page"] = context["next_page"]
        return context
