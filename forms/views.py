from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdoptionForm
from .forms import RescueForm
from .models import Adoption
from .models import Rescue


@login_required
def adoptionForm(request):
    if request.method == "POST":
        form = AdoptionForm(request.POST, request.FILES)
        if form.is_valid():
            adoption_form = form.save(commit=False)
            adoption_form.user = request.user
            adoption_form.save()
            messages.success(request, f'We have received your adoption form. Our volunteer will contact you soon.')
            return redirect('adoptionForm')
    else:
        form = AdoptionForm()

    return render(request, 'forms/adoption/adoptionForm.html', {'form': form})


@login_required
def rescueForm(request):
    if request.method == "POST":
        form = RescueForm(request.POST, request.FILES)
        if form.is_valid():
            rescue_form = form.save(commit=False)
            rescue_form.user = request.user
            rescue_form.save()
            messages.success(request, f'We have received your rescue form. Our volunteer will contact you soon.')
            return redirect('rescueForm')
    else:
        form = RescueForm()

    return render(request, 'forms/rescue/rescueForm.html', {'form': form})


@user_passes_test(lambda u:u.is_staff)
def submittedRescueForm(request):
    info = Rescue.objects.all()
    return render(request, 'forms/rescue/submittedForm.html', {'info': info})


@user_passes_test(lambda u:u.is_staff)
def submittedAdoptionForm(request):
    info = Adoption.objects.all()
    return render(request, 'forms/adoption/submittedForm.html', {'info': info})


@user_passes_test(lambda u:u.is_staff)
def adoptionFormDetails(request, form_id):
    searched = get_object_or_404(Adoption, id=form_id)
    return render(request, 'forms/adoption/formDetails.html', {'result': searched})


@user_passes_test(lambda u:u.is_staff)
def rescueFormDetails(request, form_id):
    searched = get_object_or_404(Rescue, id=form_id)
    return render(request, 'forms/rescue/formDetails.html', {'result': searched})
