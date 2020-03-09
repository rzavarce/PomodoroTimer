from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions

from .models import Task
from configs.models import Config
from .serializers import TaskSerializer

from django.contrib.auth.models import User

import json

# Create your views here.




def Index(request):

	return render(request, 'tasks/index.html', {'bikes': 'is_mobile'})

	#return HttpResponse("Hello, world. You're at the polls index.")




def PodomoroManager(request):

    context={}
    context['tasks'] = Task.objects.filter(tsk_status=0) 

    print(context['tasks'])

    return render(request, 'tasks/manager.html', context) 


def TaskList(request):

    context={}
    context['tasks'] = Task.objects.all().values('tsk_title', 'tsk_description', 'tsk_status', 'tsk_assignted_time', 'tsk_created_date')

    return render(request, 'tasks/task_list.html', context) 


def Contacts(request):

	return render(request, 'tasks/contacts.html', {'bikes': 'is_mobile'})



def ContactSendEmail(request):

fromJs = request.body

    print(request.POST)

    name = request.POST['name']
    email = request.POST.get('email')
    message = request.POST.get('message')

    print(name, email, message)

    #email = EmailMessage('New Contact message', 'THIS IS A TEST MESSAGE TO POMODORO APP', to = [ email ])


    email = EmailMessage('New Contact message', 'Name: '+ name + '\n' + 'Message: ' + message, to = [ email ])
    
    email.send()

    json_array = {"mesage":"Send Email"}


    return JsonResponse(json_array, safe=False)




class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.filter(tsk_status=0)
    serializer_class = TaskSerializer
    ordering_fields = ('id',)
    ordering = ('id',)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



