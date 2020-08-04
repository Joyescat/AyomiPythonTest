from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from authentication.models import User
from .forms import EditUserForm

def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user
    }
    if (request.POST):
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            try:
                user.email = request.POST['email']
                user.save()
            except:
                context['error_message'] = 'Impossible de modifier l\'email de l\'utilisateur'
    else:
        form = EditUserForm()
    context['form'] = form
    return HttpResponse(render(request, 'user/index.html', context))
