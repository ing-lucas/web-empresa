from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def Contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Suponiendo que todo esta bien
            email = EmailMessage(
                "La Cafeteria: nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["django@hektorproge.net"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse("contact")+"?ok")
            except:
                return redirect(reverse("contact")+"?fail")


    return render(request, "contact/contact.html",{'form':contact_form})