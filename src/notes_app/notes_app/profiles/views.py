from django.shortcuts import render, redirect

from notes_app.common.profile_utils import get_profile
from notes_app.notes.models import Note
from notes_app.profiles.forms import CreateProfileForm


def profile_details(request):
    profile = get_profile()
    if profile:
        notes_count = Note.objects.count()
        context = {
            'profile': profile,
            'notes_count': notes_count,
        }
        return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home')
