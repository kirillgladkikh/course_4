from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('mailing:home_view')  # перенаправление на главную

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mailing:home_view')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# from django.shortcuts import render
#
# # Create your views here.
# # TEST
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Привет из приложения users!")
