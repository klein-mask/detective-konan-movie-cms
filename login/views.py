from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.forms import UserCreationForm
from login.forms import MyUserCreationForm, MyAuthenticationForm
from django.contrib.auth.models import User

class LoginIndexView(TemplateView):
	template_name = 'login/index.html'

index = LoginIndexView.as_view()



class CreateAccountView(CreateView):
    def post(self, request, *args, **kwargs):
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('app:movie_list')
        return render(request, 'login/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = MyUserCreationForm(request.POST)
        return  render(request, 'login/create.html', {'form': form,})

create_account = CreateAccountView.as_view()

#ログイン機能
class AccountLoginView(View):
    def post(self, request, *arg, **kwargs):
        form = MyAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('login:login_index')

        return render(request, 'login/user.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = MyAuthenticationForm(request.POST)
        return render(request, 'login/user.html', {'form': form,})

login_account = AccountLoginView.as_view()


def logout_request(request):
    logout(request)
    print(request,"Logged out,please come back again.")
    return redirect('login:login_index')