from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

'''
from django.contrib.auth.decorators import login_required

@login_required # ログイン後に動く関数の前につける
'''


from account.models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


# Create your views here.


class Output(TemplateView):
    template_name = "output.html"
    def get(self, request, *args, **kwargs):
        context = super(Output, self).get_context_data(**kwargs)
        workers = Buy.objects.all()  # データベースからオブジェクトを取得して
        context['workers'] = workers  # 入れ物に入れる
        return render(self.request, self.template_name, context)