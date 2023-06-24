from django.shortcuts import render, redirect

from FruitipediaApp.fruit_app.forms import CreateFruitForm
from FruitipediaApp.fruit_app.models import FruitModel


# Create your views here.
def fruit_create(request):
    form = CreateFruitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'fruit_app/create-fruit.html', {'form': form})


def fruit_details(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    return render(request, "fruit_app/details-fruit.html", {'fruit': fruit})


def fruit_edit(request, pk):
    return render(request, "fruit_app/edit-fruit.html")


def fruit_delete(request, pk):
    return render(request, 'fruit_app/delete-fruit.html')
