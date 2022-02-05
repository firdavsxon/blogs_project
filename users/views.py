from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserAuthenticationForm


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user_name = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now login using this form!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


def login(request):
	form = UserAuthenticationForm(request.POST)
	return render(request, 'users/login.html', {'form': form})

