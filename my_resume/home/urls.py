from django.urls import path
from .views import *

name_apps = 'test_app'

urlpatterns = [
    path('', smth, name='smth'),
    path('index/', index, name='index')
    #path('connect/', LeadCreationView.as_view(template_name="test_telega.html")),
]