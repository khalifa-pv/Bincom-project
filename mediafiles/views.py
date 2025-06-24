from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Image
from .forms import ImageForm
from .forms import UserRegistrationForm
from .forms import EmailOrUsernameLoginForm


@login_required
def image_gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()

    images = Image.objects.all()
    return render(request, 'gallery.html', {'form': form, 'images': images})


@login_required
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.image.delete()  # Delete the file from media folder
    image.delete()        # Delete from database
    return redirect('gallery')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('gallery')
        else:           # If the form is not valid, it will contain errors
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_login_view(request):
    if request.method == 'POST':
        form = EmailOrUsernameLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('home')
    else:
        form = EmailOrUsernameLoginForm()
    return render(request, 'login.html', {'form': form})