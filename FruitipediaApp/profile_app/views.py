from django.shortcuts import render, redirect

from FruitipediaApp.profile_app.forms import CreateProfileForm
from FruitipediaApp.profile_app.models import ProfileModel


# Create your views here.
def profile_create(request):
    profile = ProfileModel.objects.first()

    # just in case, in order to prevent second profile creation via direct url input
    if profile:
        return redirect('dashboard')
    form = CreateProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'profile_app/create-profile.html', {'form': form})


def profile_details(request):
    return render(request, 'profile_app/details-profile.html')


def profile_edit(request):
    return render(request, 'profile_app/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile_app/delete-profile.html')
