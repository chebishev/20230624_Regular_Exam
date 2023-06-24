from django.shortcuts import render


# Create your views here.
def profile_create(request):
    return render(request, 'profile_app/create-profile.html')


def profile_details(request):
    return render(request, 'profile_app/details-profile.html')


def profile_edit(request):
    return render(request, 'profile_app/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile_app/delete-profile.html')
