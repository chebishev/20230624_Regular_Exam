from django.shortcuts import render


# Create your views here.
def fruit_create(request):
    return render(request, 'fruit_app/create-fruit.html')


def fruit_details(request):
    return render(request, "fruit_app/details-fruit.html")


def fruit_edit(request):
    return render(request, "fruit_app/edit-fruit.html")


def fruit_delete(request):
    return render(request, 'fruit_app/delete-fruit.html')
