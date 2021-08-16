from django.shortcuts import render
from .models import Contact
from About.models import About
# Create your views here.

def ContactView(request):

    about = About.objects.all()[:3]

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name,email=email,phone=tel,subject=subject,msg=message)
        contact.save()
        return render(request,'contact.html',)
    
    return render(request, 'contact.html',{'about':about})

