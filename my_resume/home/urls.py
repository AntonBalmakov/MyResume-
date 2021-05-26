from django.conf.urls.static import static
from django.urls import path
from django_countries import settings

from .views import *

name_apps = 'test_app'

urlpatterns = [

    # path('index_test/', index_test, name='index'),
    path('', index, name='index')
    #path('connect/', LeadCreationView.as_view(template_name="test_telega.html")),
]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)