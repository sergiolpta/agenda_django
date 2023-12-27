from django.shortcuts import render, redirect
from core.models import Evento

# código para acessar a pagina inicial direto na agenda
# def index(request):
#     return redirect('/agenda/')

# Create your views here.
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)