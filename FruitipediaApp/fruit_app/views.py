from django.shortcuts import render, redirect

from FruitipediaApp.fruit_app.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
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
    fruit = FruitModel.objects.get(pk=pk)
    form = EditFruitForm(request.POST or None, instance=fruit)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, "fruit_app/edit-fruit.html", context)


def fruit_delete(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')
    form = DeleteFruitForm(instance=fruit)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = True
    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruit_app/delete-fruit.html', context)
