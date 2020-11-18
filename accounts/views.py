from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UsersLoginForm
from django.contrib.auth import authenticate, login ,logout
from .forms import UsersRegisterForm
from django.http import HttpResponseRedirect


def login_view(request):
	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return redirect("/blog/")
	return render(request, "forms.html", {
		"form" : form,
		"title" : "Login",
	})


def register_view(request):
	form = UsersRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get("password")	
		user.set_password(password)
		user.save()
		new_user = authenticate(username = user.username, password = password)
		login(request, new_user)
		return redirect("/accounts/login")
	return render(request, "forms.html", {
		"title" : "Register",
		"form" : form,
	})


def logout_view(request):
	logout(request)
	return redirect("/accounts/login")