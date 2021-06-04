
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from django.views.generic import CreateView
#from .telegramm import send_message
from .forms import ContactForm
from .models import *

def index(request):
    name = Name.objects.all()
    skill = Skills.objects.all()
    study = Study.objects.all()
    himself = Himself.objects.all()
    certificate = Certificates.objects.all()
    project = Projects.objects.all()
    context = {'name': name,
               'skill': skill,
               'study': study,
               'himself': himself,
               'certificate': certificate,
               'project': project,}
    return render(request, 'index.html', context)