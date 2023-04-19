import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import FeriadoModel
from datetime import date

date = datetime.date.today()

def natal(request):
    if date.day == 25 and date.month == 12:
        contexto = {'natal': True}
        return render(request, 'natal.html', contexto)
    else:
        contexto = {'natal': False} 
        return render(request, 'natal.html', contexto)
    
def tiradentes(request):
    if date.day == 21 and date.month == 4:
        contexto = {'tiradentes': True}
        return render(request, 'tiradentes.html', contexto)
    else:
        contexto = {'tiradentes': False}
        return render(request, 'tiradentes.html', contexto)
    
def feriado(request):
  hoje = date.today()

  qs = FeriadoModel.objects.filter(dia=hoje.day)
  qs = qs.filter(mes=hoje.month)

  if qs.exists():
    contexto = {'nome': qs[0].nome}
    return render(request, 'feriado.html', contexto)
  elif hoje.weekday() == 2:
    return render(request, 'feriado.html')
# Create your views here.
