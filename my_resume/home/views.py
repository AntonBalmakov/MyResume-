from django.shortcuts import render, redirect
from django.views.generic import CreateView
#from .telegramm import send_message
from .forms import ContactForm
from .models import *


# class LeadCreationView(CreateView):
#     form_class = ContactForm
#     # success_url = reverse_lazy('callback')
#
#     def form_valid(self, form):
#         name = form.cleaned_data['name']
#         # phone = form.cleaned_data['phone']
#         message_hr = form.cleaned_data['message_hr']
#         message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " + str(name) + "\n" + "*СООБЩЕНИЕ*" + str(message_hr)
#         send_message(message)
#         return super(LeadCreationView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         return redirect(self.get_success_url())

# def index_test(request):
#     name = Name.objects.all()
#     skill = Skills.objects.all()
#     study = Study.objects.all()
#     himself = Himself.objects.all()
#     certificate = Certificates.objects.all()
#     project = Projects.objects.all()
#     context = {'name': name,
#                'skill': skill,
#                'study': study,
#                'himself': himself,
#                'certificate': certificate,
#                'project': project, }
#     return render(request, 'index_test.html', context)


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
               'project': project, }
    return render(request, 'index.html', context)