from django.shortcuts import render, redirect

from FruitipediaApp.profile_app.forms import CreateProfileForm


# Create your views here.
def profile_create(request):
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
