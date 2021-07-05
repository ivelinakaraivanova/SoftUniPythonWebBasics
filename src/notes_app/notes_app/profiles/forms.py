from django import forms

from notes_app.common.forms_labels_suffix import BaseModelForm
from notes_app.profiles.models import Profile


class ProfileForm(BaseModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image'
        }


class CreateProfileForm(ProfileForm):
    pass
