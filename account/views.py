from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from django.contrib.auth import login
from django.contrib.auth import authenticate

from account.models import *

class CustomLoginView(TemplateView):
    template_name = "login.html"

    def get(self, _, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return login(self.request, *args, **kwargs)

    def post(self, _, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)  # 1
        if user is not None:
            login(self.request, user)
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return login(self.request, *args, **kwargs)

    def get_next_redirect_url(self):
        redirect_url = self.request.GET.get('next')
        if not redirect_url or redirect_url == '/':
            redirect_url = '/house_account/'
        return redirect_url

# Create your views here.


class Output(TemplateView):
    template_name = "output.html"
    def get(self, request, *args, **kwargs):
        context = super(Output, self).get_context_data(**kwargs)
        workers = Buy.objects.all()  # データベースからオブジェクトを取得して
        context['workers'] = workers  # 入れ物に入れる
        return render(self.request, self.template_name, context)