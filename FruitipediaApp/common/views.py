from django.shortcuts import render

from FruitipediaApp.fruit_app.models import FruitModel


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = FruitModel.objects.all()
    return render(request, 'common/dashboard.html', {'fruits': fruits})
