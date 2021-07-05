from django import forms

from notes_app.common.forms_labels_suffix import BaseModelForm
from notes_app.notes.models import Note


class NoteForm(BaseModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image_url': 'Link to Image'
        }


class CreateNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
