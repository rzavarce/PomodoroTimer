from django.shortcuts import render
from django.http import HttpResponse, Http404

from .serializers import UserSerializer

from rest_framework import viewsets
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer

from django.contrib.auth.models import User

# Create your views here.




def Index(request):

	return render(request, 'tasks/index.html', {'bikes': 'is_mobile'})

	#return HttpResponse("Hello, world. You're at the polls index.")




def PodomoroManager(request):

	return render(request, 'tasks/manager.html', {'bikes': 'is_mobile'})

	#client = Client.objects.filter(users__id=request.user.id) 
	#bikes = Bike.objects.filter(client__owner = request.user, device__status=0)

	#return render(request, 'templates/index.html', {'bikes': 'is_mobile'})





def Contacts(request):

	return render(request, 'tasks/contacts.html', {'bikes': 'is_mobile'})




class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



