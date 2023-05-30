from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomDriverForm
from .models import Driver


def driver_list(request):
    template_name = 'driver/driver_list.html'
    object_list = Driver.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def driver_create(request):
    template_name = 'driver/driver_form.html'
    form = CustomDriverForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('drive:drive_list')

    context = {'form': form}
    return render(request, template_name, context)


def driver_detail(request, pk):
    template_name = 'driver/driver_detail.html'
    instance = get_object_or_404(Driver, pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def driver_update(request, pk):
    template_name = 'driver/driver_form.html'
    instance = get_object_or_404(Driver, pk=pk)
    form = CustomDriverForm(request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('driver:driver_list')

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


def driver_delete(request, pk):
    instance = get_object_or_404(Driver, pk=pk)
    instance.delete()
    return redirect('driver:driver_list')
