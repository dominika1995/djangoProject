from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ShortDescription, MyEmailAddress


def email_view(request):
    text = ShortDescription.objects.all()[0].text
    email = MyEmailAddress.objects.all()[0].eMail
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "../templates/contact.html", {'form': form, 'text': text})


def success_view(request):
    text = ShortDescription.objects.all()[0].text
    return render(request, "../templates/contact.html",
                  {'success': 'Success! Thank you for your message.', 'text': text})

