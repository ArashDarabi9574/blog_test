from .forms import MyUserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from .task import sendemail
from django.http import HttpResponse, JsonResponse
import requests
from django.views.decorators.cache import cache_page

# Create your views here.


@cache_page(60)
def test(req):
    response = requests.get(
        "https://fe8703fd-70c2-402e-9166-7033a00ee268.mock.pstmn.io/delay/5"
    )
    return JsonResponse(response.json())


def send_email(request):
    sendemail.delay()
    return HttpResponse("Done!!!!!!!!!!!!!")


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "username", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("task_list")


class RegisterPage(FormView):
    template_name = "accounts/register.html"
    form_class = MyUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task_list")
        return super(RegisterPage, self).get(*args, **kwargs)
