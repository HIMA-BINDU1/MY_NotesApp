from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Note


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            login(request, form.get_user())
            return redirect('notes')
    else:
        form = AuthenticationForm()
    return render(request, 'notes/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def notes_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(user=request.user, title=title, content=content)
        return redirect('notes')

    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/notes.html', {'notes': notes})

@login_required
def delete_note(request, note_id):
    Note.objects.get(id=note_id, user=request.user).delete()
    return redirect('notes')
