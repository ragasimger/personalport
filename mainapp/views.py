from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from decouple import config


def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method != "POST":
        return HttpResponse('Method not allowed')
    name = request.POST['name']
    emailname = request.POST['email']
    phonenum = request.POST['phonenum']
    subject = request.POST['subject']
    message = request.POST['message']
    send_mail('New Mail on Portfolio from' + '  ' + name + ' ' + 'on' + ' ' + subject, (((f"His/her email: {emailname}" + "\nPhone Number: " + phonenum) + "\n Message starts from here:\n\n") + message), emailname, [config("EMAIL_ID")], fail_silently=False)

    params = {'name': name}
    return render(request, 'contact.html', params)
