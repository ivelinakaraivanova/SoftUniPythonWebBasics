from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from todo_project.todo_app.models import Todo


# def validate_dot(value):
#     if '.' in value:
#         raise forms.ValidationError("'.' is present in value")
#
from todo_project.todo_app.validators import validate_owner_todos_count


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__'
        # fields = ['title', 'state', 'description', 'owner']
        exclude = ('categories',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'owner': forms.RadioSelect()
        }

    def clean(self):
        validate_owner_todos_count(self.cleaned_data['owner'])


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