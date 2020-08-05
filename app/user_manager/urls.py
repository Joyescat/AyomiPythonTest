from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/(?P<user_id>[0-9]+)$', views.update_user, name='user'),
]
