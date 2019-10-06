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


def proyectos(request):
    return render(request, "core/proyectos.html")

def proyecto(request):
    return render(request, "core/proyecto.html")

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
            tipo = form.data["tipo"]
            nombre = form.data["txtName"]
            mail = form.data["txtEmail"]
            telefono = form.data["txtPhone"]
            direccion = form.data["txtSubject"]
            detalle = form.data["txtMsg"]
            asunto = ""
            td = ""
            if tipo == "express":
                asunto = "Solicitud de Presupuesto Express"
                td = "Dirección"
            else:
                asunto = "Contacto"
                td = "Asunto"
            mensaje = """<table width="100%" border="1" cellpadding="7" cellspacing="0" bordercolor="#CCCCCC">
  <tr>
    <td>&nbsp;&nbsp;Nombre</td>
    <td>"""+nombre+"""</td>
  </tr>
  <tr>
    <td bgcolor="#f1f1f1">&nbsp;&nbsp;Mail</td>
    <td bgcolor="#f1f1f1">"""+mail+"""</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;Telefono</td>
    <td>"""+telefono+"""</td>
  </tr>
  <tr>
    <td bgcolor="#f1f1f1">"""+td+"""</td>
    <td bgcolor="#f1f1f1">"""+direccion+"""</td>
  </tr>
   <tr>
    <td>&nbsp;&nbsp;Detalle</td>
    <td>"""+detalle+"""</td>
  </tr>
</table> """

            send_mail(asunto,
                      "probando mensaje",
                      "symphony.of.all@gmail.com",
                      ["nickolas.rivera.catalan@gmail.com"],
                      fail_silently=False, html_message=mensaje)
            return HttpResponse('exito')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = contacto()

    return HttpResponse('fracaso')
