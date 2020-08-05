from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from authentication.models import User
from .forms import EditUserForm
import json

def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user
    }
    if (request.POST):
        form = EditUserForm(request.POST, instance=user)
        response_data = {}
        if form.is_valid():
            user = form.save()
            response_data['result'] = 'SUCCESS'
            response_data['email'] = user.email
        else:
            response_data['error_message'] = 'Cette addresse e-mail est déjà associée à un compte ou est invalide'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        form = EditUserForm(instance=user)
    context['form'] = form
    return HttpResponse(render(request, 'user/index.html', context))
