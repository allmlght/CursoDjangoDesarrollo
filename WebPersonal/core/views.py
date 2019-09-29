from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .form import contacto
# Create your views here.


def home(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def mensajecontacto(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = contacto(data=request.POST)
        print(form.is_valid())
        print(form.data)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(form.cleaned_data["txtSubject"])
            print(form.cleaned_data["txtMsg"])
            print("nickolas.rivera.catalan@gmail.com")
            print(form.cleaned_data["txtEmail"])
            send_mail(form.cleaned_data["txtSubject"],
            form.cleaned_data["txtEmail"],
            "symphony.of.all@gmail.com",
            ["nickolas.rivera.catalan@gmail.com"],
            fail_silently=False)
            return HttpResponse('exito')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = contacto()

    return HttpResponse('fracaso')
