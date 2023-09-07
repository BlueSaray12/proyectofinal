from django.shortcuts import render, redirect
from django.urls import reverse
from . forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contactForm=ContactForm()
    if request.method=="POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            subject=request.POST.get('subject', '')
            message=request.POST.get('message', '')

            emailContact = EmailMessage(
            "CAKEZONE",
            "De {} <{}> \n\nMensaje:\n\n{}".format(name, email, message),  
            "blue12@gmail.com",
            ["Correo-proyecto@inbox.mailtrap.io"],
            reply_to=[email]
)         
            try:
              emailContact.send()
              return redirect(reverse('contact')+"?ok")
            except:
              return redirect(reverse('contact')+"?fail")
            
    return render(request, "contact/contact.html", {'contactForm':contactForm})

