from django.shortcuts import render
from django.http import HttpResponse


def user(request, user_id):
    return HttpResponse("Hello, world. You're at the polls index.")
