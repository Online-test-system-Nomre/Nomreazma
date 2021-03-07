from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quez/getresponses', views.getresponses),
    url(r'^quez/postresponses', views.postresponses)
]
