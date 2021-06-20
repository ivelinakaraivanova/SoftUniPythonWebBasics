# cities.urls
from django.urls import path

from djangoloto.cities.views import index, list_phones, test_index, create_person, show_forms_demo

urlpatterns = [
    path('', index),  # /'cities/' + '' = '/cities/'
    path('create/', create_person, name='create person'),
    path('test/', test_index),
    path('phones/', list_phones),  # /'' + 'phones/' = '/cities  /phones/'
    path('forms/', show_forms_demo),
]