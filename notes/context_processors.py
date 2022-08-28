from django.contrib.auth.forms import AuthenticationForm


def include_login_form(request):
    login = AuthenticationForm()

    return {'login': login}
