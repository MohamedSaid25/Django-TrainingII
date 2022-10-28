from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginForm
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login
# Create your views here.


class RegistrationForm(FormView):
    form_class = CreateUserForm
    template_name = 'accounts/register.html'
    success_url = 'login'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return super().form_valid(form)


class LoginPageView(View):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('artists')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
