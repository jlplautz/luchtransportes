from django.shortcuts import get_object_or_404, render

from .forms import CustomFreightForm
from .models import Freight


def freight_list(request):
    template_name = 'freight/freight_list.html'
    object_list = Freight.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def freight_create(request):
    template_name = 'freight/freight_form.html'
    form = CustomFreightForm(request.POST or None)
    context = {'form': form}
    return render(request, template_name, context)


def freight_detail(request, pk):
    template_name = 'freight/freight_detail.html'
    instance = get_object_or_404(Freight, pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def freight_update(request, pk):
    template_name = 'freight/freight_form.html'
    instance = get_object_or_404(Freight, pk=pk)
    form = CustomFreightForm(request.POST or None, instance=instance)

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)
