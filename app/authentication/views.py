from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User

def login(request):
	context = {}
	if (request.POST):
		try:
			user = get_object_or_404(User, email=request.POST['email'], password=request.POST['password'])
			return HttpResponseRedirect(reverse('user_manager:user', args=(user.id,)))
		except:
			context['error_message'] = 'Email ou mot de passe erroné'

	return HttpResponse(render(request, 'login/index.html', context))

def register(request):
	context = {}
	if (request.POST):
		try:
			user = User(email=request.POST['email'], password=request.POST['password'])
			user.save()
			return HttpResponseRedirect(reverse('authentication:login'))
		except:
			context['error_message'] = 'Un compte avec cette address e-mail est déjà existant'

	return HttpResponse(render(request, 'register/index.html', context))
