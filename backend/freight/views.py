# from django.views.generic import ListView <- qdo usamos ListView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomFreightForm, FreightFeeForm
from .models import Freight, FreightFee

# class FreightListView(ListView):
#     model = Freight
#     paginate_by = 5


def freight_list(request):
    template_name = 'freight/freight_list.html'
    object_list = Freight.objects.all()

    search = request.GET.get('search')

    if search:
        print(search)
        object_list = object_list.filter(
            Q(data__icontains=search)
            | Q(caminhao__placa__icontains=search)
            | Q(frete_adiant_valor__icontains=search)
            | Q(frete_saldo_valor__icontains=search)
            | Q(origem__icontains=search)
            | Q(destino__icontains=search)
            | Q(data__icontains=search)
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


def freightfee_list(request):
    template_name = 'freight/freightfee_list.html'
    object_list = FreightFee.objects.all()
    # context = {'object_list': object_list}

    search = request.GET.get('search')

    if search:
        object_list = object_list.filter(
            Q(data__icontains=search)
            | Q(caminhao__placa__icontains=search)
            | Q(valor_adiant_fixo__icontains=search)
            | Q(valor_saldo_fixo__icontains=search)
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


def freight_create(request):
    template_name = 'freight/freight_form.html'
    form = CustomFreightForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('freight:freight_list')

    verbose_name_plural = form.instance._meta.verbose_name_plural

    context = {'form': form, 'verbose_name_plural': verbose_name_plural}

    return render(request, template_name, context)


def freightfee_create(request):
    template_name = 'freight/freightfee_form.html'
    form = FreightFeeForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('freight:freightfee_list')

    verbose_name_plural = form.instance._meta.verbose_name_plural

    context = {'form': form, 'verbose_name_plural': verbose_name_plural}

    return render(request, template_name, context)


def freight_detail(request, pk):
    template_name = 'freight/freight_detail.html'
    instance = get_object_or_404(Freight, pk=pk)
    print(instance.id)
    context = {'object': instance}
    return render(request, template_name, context)


def freightfee_detail(request, pk):
    template_name = 'freight/freightfee_detail.html'
    instance = get_object_or_404(FreightFee, pk=pk)
    print(instance.id)
    context = {'object': instance}
    return render(request, template_name, context)


def freight_update(request, pk):
    template_name = 'freight/freight_form.html'
    instance = get_object_or_404(Freight, pk=pk)
    form = CustomFreightForm(request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('freight:freight_list')

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


def feeupdate(request, pk):
    template_name = 'freight/freightfee_form.html'
    instance = get_object_or_404(FreightFee, pk=pk)
    form = FreightFeeForm(request.POST or None, instance=instance)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('freight:freightfee_list')

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


def freight_delete(request, pk):
    instance = get_object_or_404(Freight, pk=pk)
    print(instance.pk)
    instance.delete()
    return redirect('freight:freight_list')


def feedelete(request, pk):
    instance = get_object_or_404(FreightFee, pk=pk)
    print(instance.pk)
    instance.delete()
    return redirect('freight:freightfee_list')
