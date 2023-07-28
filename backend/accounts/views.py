# accounts/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
)
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomUserForm
from .models import User

# from backend.accounts.services import send_mail_to_user


@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)


def signup(request):
    """
    Cadastra Usuário.
    """
    template_name = 'registration/registration_form.html'
    form = CustomUserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            # send_mail_to_user(request=request, user=user)
            return redirect('login')

    return render(request, template_name)


class MyPasswordResetConfirm(PasswordResetConfirmView):
    """
    Requer password_reset_confirm.html
    """

    def form_valid(self, form):
        self.user.is_active = True
        self.user.save()
        return super(MyPasswordResetConfirm, self).form_valid(form)


class MyPasswordResetComplete(PasswordResetCompleteView):
    """
    Requer password_reset_complete.html
    """


def user_list(request):
    template_name = 'accounts/user_list.html'
    object_list = User.objects.exclude(email='admin@email.com')
    # context = {'object_list': object_list}

    search = request.GET.get('search')

    if search:
        print(search)
        object_list = object_list.filter(
            Q(email__icontains=search)
            | Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
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


def user_detail(request, pk):
    template_name = 'accounts/user_detail.html'
    instance = get_object_or_404(User, pk=pk)
    context = {'object': instance}
    return render(request, template_name, context)


def user_create(request):
    template_name = 'accounts/user_form.html'
    form = CustomUserForm(request.POST or None)
    context = {'form': form}
    return render(request, template_name, context)


def user_update(request, pk):
    template_name = 'accounts/user_form.html'
    instance = get_object_or_404(User, pk=pk)
    form = CustomUserForm(request.POST or None, instance=instance)

    context = {
        'object': instance,
        'form': form,
    }
    return render(request, template_name, context)


def user_delete(request, pk):
    # user = User.objects.get(pk=pk)
    instance = get_object_or_404(User, pk=pk)
    instance.delete()
    # user.delete()
    # return redirect('accounts/user_list.html')
    template_name = 'accounts/user_list.html'
    return render(request, template_name)
