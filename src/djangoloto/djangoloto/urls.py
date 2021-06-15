from django.contrib import admin
from django.urls import path, include

from djangoloto.cities.views import index, list_phones

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('cities/', include('djangoloto.cities.urls')),
    path('', include('djangoloto.people.urls')),

    # path('cities/', index),
    # path('cities/phones/', list_phones)
]
