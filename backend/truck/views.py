from django.shortcuts import get_object_or_404, render

from .forms import CustomTruckFeesForm, CustomTruckForm
from .models import Truck, TruckFees


def truck_list(request):
    template_name = 'truck/truck_list.html'
    object_list = Truck.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def truckfees_list(request):
    template_name = 'truck/truckfees_list.html'
    object_list = TruckFees.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def truck_create(request):
    template_name = 'truck/truck_form.html'
    form = CustomTruckForm(request.POST or None)
    context = {'form': form}
    return render(request, template_name, context)


def truckfees_create(request):
    template_name = 'truck/truckfees_form.html'
    form = CustomTruckFeesForm(request.POST or None)
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
