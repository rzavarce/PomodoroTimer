from django.shortcuts import render

from .forms import  

# Create your views here.


def Contacts(request):
	form = ContactForm()

	return render(request, 'tasks/contacts.html', {'form': form})





def ContactSendEmail(request):

    print(request.POST)

    name = request.POST['name']
    email = request.POST.get('email')
    message = request.POST.get('message')

    print(name, email, message)

    email = EmailMessage('New Contact message', 'THIS IS A TEST MESSAGE TO POMODORO APP', to = [ email ])


    #email = EmailMessage('New Contact message', 'Name: '+ name + '\n' + 'Message: ' + message, to = [ email ])
    
    email.send()

    json_array = {"mesage":"Send Email"}


    return JsonResponse(json_array, safe=False)








