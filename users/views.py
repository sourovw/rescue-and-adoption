from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileCreationForm
from django.contrib import messages
from .models import Profile


def registrationPage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. Now you are able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def createProfile(request):
    if request.method == "POST":
        form = ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, f'Profile created successfully.')
            return redirect('showProfiles')
    else:
        form = ProfileCreationForm()

    return render(request, 'users/createProfile.html', {'form': form})


@login_required
def showProfiles(request):
    order = request.GET.get('order', 'desc')
    profiles = Profile.objects.all()

    if (order == 'desc'):
        profiles = profiles.order_by('-id')
    elif (order == 'desc'):
        profiles = profiles.order_by('id')

    return render(request, 'users/showProfiles.html', {'profiles': profiles})


@login_required
def profileDetails(request, profile_id):
    searched = get_object_or_404(Profile, id=profile_id)
    return render(request, 'users/profile.html', {'result': searched})


def home(request):
    return render(request, 'home.html')
