from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from authentication.models import User

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user
    }
    if (request.POST):
        try:
            user.email = request.POST['email']
            user.save()
        except:
            context['error_message'] = 'Impossible de modifier l\'email de l\'utilisateur'
    return HttpResponse(render(request, 'user/index.html', context))
