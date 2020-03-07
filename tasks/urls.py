#from django.urls import url, path
from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.PodomoroManager, name='index'),

    url(r'', views.Index, name='index'),

    url(r'Start/', views.PodomoroManager, name='pomodoro_manager'),







]