"""PomodoroApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from tasks import views as tasks

router = routers.DefaultRouter()
router.register(r'users', tasks.UserViewSet)
router.register(r'tasks', tasks.TaskViewSet)
#router.register(r'tasks/{pk}', tasks.TaskDetails)


urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', tasks.Index, name='index'),

    url(r'Manager/', tasks.PodomoroManager, name='pomodoro_manager'),

    url(r'TaskList/', tasks.TaskList, name='task_list'),


    url(r'Contact/', tasks.Contacts, name='contact'),

    url(r'ContactSendEmail/', tasks.ContactSendEmail, name='send_email'),

    url(r'^', include(router.urls))


]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
