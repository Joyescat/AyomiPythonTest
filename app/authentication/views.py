from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User

def login(request):
    return HttpResponse(render(request, 'login/index.html'))

def postLogin(request):
	user = get_object_or_404(User, email=request.POST['email'], password=request.POST['password'])
	print(user)
	return HttpResponseRedirect(reverse('userManager:user', args=(user.id,)))

def register(request):
    return HttpResponse(render(request, 'register/index.html'))
