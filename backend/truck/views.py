from django.shortcuts import get_object_or_404, render

from .forms import CustomTruckForm
from .models import Truck


def truck_list(request):
    template_name = 'truck/truck_list.html'
    object_list = Truck.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def truck_create(request):
    template_name = 'truck/truck_form.html'
    form = CustomTruckForm(request.POST or None)
    context = {'form': form}
    return render(request, template_name, context)


def truck_detail(request, pk):
    template_name = 'truck/truck_detail.html'
    instance = get_object_or_404(Truck, pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def truck_update(request, pk):
    template_name = 'truck/truck_form.html'
    instance = get_object_or_404(Truck, pk=pk)
    form = CustomTruckForm(request.POST or None, instance=instance)

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)
