from django.shortcuts import render, redirect

from petstagram.main_app.forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import Pet


def pet_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'pet': instance,
    }

    return render(request, template_name, context)


def add_pet(request):
    return pet_action(request, CreatePetForm, 'profile', Pet(user_profile=get_profile()), 'pet_create.html')


def edit_pet(request, pk):
    return pet_action(request, EditPetForm, 'profile', Pet.objects.get(pk=pk), 'pet_edit.html')


def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'pet_delete.html')
