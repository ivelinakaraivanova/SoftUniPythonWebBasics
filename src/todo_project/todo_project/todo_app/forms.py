from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


def validate_dot(value):
    if '.' in value:
        raise forms.ValidationError("'.' is present in value")


class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        validators=[
            validate_dot,
            # MinValueValidator(3),
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter todo text',
            }
        )
    )

    # state = forms.BooleanField()
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'my-text-area',
            }
        )
    )

    bots_catcher = forms.CharField(
        widget= forms.HiddenInput(),
        required=False,
    )

    def clean_bots_catcher(self):
        value = self.cleaned_data['bots_catcher']

        if value:
            raise ValidationError('You are a bot')


class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField()