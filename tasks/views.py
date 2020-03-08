from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions

from .models import Task
from configs.models import Config
from .serializers import TaskSerializer

from django.contrib.auth.models import User

# Create your views here.




def Index(request):

	return render(request, 'tasks/index.html', {'bikes': 'is_mobile'})

	#return HttpResponse("Hello, world. You're at the polls index.")




def PodomoroManager(request):

    context={}
    context['tasks'] = Task.objects.filter(tsk_status=0) 

    print(context['tasks'])

    return render(request, 'tasks/manager.html', context) 


def Contacts(request):

	return render(request, 'tasks/contacts.html', {'bikes': 'is_mobile'})




class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.filter(tsk_status=0)
    serializer_class = TaskSerializer
    ordering_fields = ('id',)
    ordering = ('id',)


'''

class TaskDetailsViewSet(APIView, pk):
    """
    API endpoint that allows users to be viewed or edited.
    """


    serializer_class = TaskSerializer
    

    try:
        queryset = Config.objects.get(pk=pk)
    except Serie.DoesNotExist:
        return HttpResponse(status=404)


@csrf_exempt
def TaskDetails(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        config = Config.objects.get(pk=pk)
    except Config.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(config)
        return JSONResponse(serializer.data)



'''


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



