from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomTruckForm, TruckFlueForm, TruckRepairForm
from .models import Truck, TruckFlue, TruckRepair


def truck_list(request):
    template_name = 'truck/truck_list.html'
    object_list = Truck.objects.all()
    # context = {'object_list': object_list}

    search = request.GET.get('search')

    if search:
        object_list = object_list.filter(
            Q(placa__icontains=search)
            | Q(marca__icontains=search)
            | Q(modelo__icontains=search)
            | Q(Chassis__icontains=search)
        )

    items_per_page = 10
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'items_count': page_obj.object_list.count(),
    }

    return render(request, template_name, context)


def truckflue_list(request):
    template_name = 'truck/truckflue_list.html'
    object_list = TruckFlue.objects.all()
    # context = {'object_list': object_list}

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(caminhao__placa__icontains=search)
            | Q(data__icontains=search)
            | Q(litros__icontains=search)
            | Q(flue_valor__icontains=search)
            | Q(cidade__icontains=search)
        )

    items_per_page = 10
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'items_count': page_obj.object_list.count(),
    }

    return render(request, template_name, context)


def truckrepair_list(request):
    template_name = 'truck/truckrepair_list.html'
    object_list = TruckRepair.objects.all()
    # context = {'object_list': object_list}

    search = request.GET.get('search')
    if search:
        object_list = object_list.filter(
            Q(caminhao__placa__icontains=search)
            | Q(data__icontains=search)
            | Q(repair_valor__icontains=search)
        )

    items_per_page = 10
    paginator = Paginator(object_list, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'items_count': page_obj.object_list.count(),
    }

    return render(request, template_name, context)


def truck_create(request):
    template_name = 'truck/truck_form.html'
    form = CustomTruckForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('truck:truck_list')

    verbose_name_plural = form.instance._meta.verbose_name_plural

    context = {'form': form, 'verbose_name_plural': verbose_name_plural}

    return render(request, template_name, context)


def truckflue_create(request):
    template_name = 'truck/truckflue_form.html'
    form = TruckFlueForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('truck:truckflue_list')

    verbose_name_plural = form.instance._meta.verbose_name_plural

    context = {'form': form, 'verbose_name_plural': verbose_name_plural}

    return render(request, template_name, context)


def truckrepair_create(request):
    template_name = 'truck/truckrepair_form.html'
    form = TruckRepairForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('truck:truckrepair_list')

    verbose_name_plural = form.instance._meta.verbose_name_plural

    context = {'form': form, 'verbose_name_plural': verbose_name_plural}

    return render(request, template_name, context)


def truck_detail(request, pk):
    template_name = 'truck/truck_detail.html'
    instance = get_object_or_404(Truck, pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def truckflue_detail(request, pk):
    template_name = 'truck/truckflue_detail.html'
    instance = get_object_or_404(TruckFlue, pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def truckrepair_detail(request, pk):
    template_name = 'truck/truckrepair_detail.html'
    instance = get_object_or_404(TruckRepair, pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def truck_update(request, pk):
    template_name = 'truck/truck_form.html'
    instance = get_object_or_404(Truck, pk=pk)
    form = CustomTruckForm(request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('truck:truck_list')

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


def flueupdate(request, pk):
    template_name = 'truck/truckflue_form.html'
    instance = get_object_or_404(TruckFlue, pk=pk)
    form = TruckFlueForm(request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('truck:truckflue_list')

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


def repairupdate(request, pk):
    template_name = 'truck/truckrepair_form.html'
    instance = get_object_or_404(TruckRepair, pk=pk)
    form = TruckRepairForm(request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('truck:truckrepair_list')

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


def truck_delete(request, pk):
    instance = get_object_or_404(Truck, pk=pk)
    instance.delete()
    return redirect('truck:truck_list')


def fluedelete(request, pk):
    instance = get_object_or_404(TruckFlue, pk=pk)
    instance.delete()
    return redirect('truck:truckflue_list')


def repairdelete(request, pk):
    instance = get_object_or_404(TruckRepair, pk=pk)
    instance.delete()
    return redirect('truck:truckrepair_list')
