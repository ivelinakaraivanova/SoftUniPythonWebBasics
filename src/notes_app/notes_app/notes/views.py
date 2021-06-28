from django.shortcuts import render, redirect

from notes_app.common.profile_utils import get_profile
from notes_app.notes.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes_app.notes.models import Note


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CreateNoteForm()

    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'note': note,
        'form': form
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form
    }

    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    if note:
        context = {
            'note': note,
        }

        return render(request, 'note-details.html', context)
