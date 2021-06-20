from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_project.todo_app.urls')),
    path('forms/', include('todo_project.forms_workshop.urls')),
]
