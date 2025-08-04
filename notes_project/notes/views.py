from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Note

# -------------------------
# User Authentication Views
# -------------------------

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


# -------------------------
# Notes Views
# -------------------------

@login_required
def notes_view(request):
    # Handle note creation
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            Note.objects.create(
                user=request.user,
                title=title,
                content=content,

            )
        return redirect('notes')

    # Handle search
    query = request.GET.get('q')
    notes = Note.objects.filter(user=request.user)

    if query:
        notes = notes.filter(title__icontains=query)

    # Separate pinned and unpinned notes
    pinned_notes = notes.filter(is_pinned=True).order_by('-id')
    unpinned_notes = notes.filter(is_pinned=False).order_by('-id')

    return render(request, 'notes/notes.html', {
        'pinned_notes': pinned_notes,
        'unpinned_notes': unpinned_notes,
    })


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('notes')


@login_required
def toggle_pin(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.is_pinned = not note.is_pinned
    note.save()
    return redirect('notes')
