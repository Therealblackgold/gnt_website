from django.shortcuts import render
from .models import Service
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def home_view(request):
    services = Service.objects.all()

    #  If method = POST Send email
    if request.method == "POST":
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']

        # Email HTML page
        html = render_to_string(
            "pages/email.html", {"subject": subject, "name": name, "email": email, "message": message, "number": number})

        send_mail(
            email,  # subject
            message,  # message
            email,  # from email
            ['nchologauta@gmail.com'],  # to email
            html_message=html,  # html page
            fail_silently=False,
        )
        return render(request, 'pages/message.html', {'name': name})
    else:
        context = {"services": services}
        return render(request, "pages/index.html", context)


def service_view(request, pk):
    service = Service.objects.get(id=pk)
    context = {"service": service}
    return render(request, "pages/service.html", context)
