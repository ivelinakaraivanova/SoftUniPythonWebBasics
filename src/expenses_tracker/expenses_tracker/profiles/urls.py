from django.urls import path

from expenses_tracker.profiles.views import profile_details, edit_profile, delete_profile, create_profile

urlpatterns = [
    path('', profile_details, name='profile info'),
    path('create/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]
