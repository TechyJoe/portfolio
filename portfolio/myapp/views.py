from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from myapp import models
from myapp.models import Contact
# Create your views here.
def index(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        print('post')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        content = request.POST.get('content','')
        number = request.POST.get('number','')


        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'length of name should be between2 and 30 characters, try again')
            return render(request, 'home.html')
        

        if len(email)>1 and len(email)<50 and '@' in email:
            pass
        else:
            messages.error(request,'length of email should be between2 and 50 characters and should contain @, try again')
            return render(request, 'home.html')
        
        if len(number)>1 and len(number)<10:
            pass
        else:
            messages.error(request,'invalid, try again')
            return render(request, 'home.html')
        
        ins=models.Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, "Thanks for contacting me|| ypur messsage has been saved successfully.")
        print("Data has been saved to the database.")
        print("The request is no pass")

    return render(request, 'home.html')