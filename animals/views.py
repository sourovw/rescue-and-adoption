from django.shortcuts import render, get_object_or_404
from .models import Animal


def showAnimals(request):
    order = request.GET.get('order', 'desc')
    result = Animal.objects.all()

    if (order == 'desc'):
        result = result.order_by('-id')
    elif (order == 'desc'):
        result = result.order_by('id')
    
    if request.method == 'POST':
        category = Animal.objects.filter(category__icontains = request.POST['search'])
        gender = Animal.objects.filter(gender__icontains = request.POST['search'])
        result = category | gender

    return render(request, 'animals/showAnimals.html', {'animals' : result})


def animalDetails(request, animal_id):
    searched = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animals/animalDetails.html', {'result': searched})
