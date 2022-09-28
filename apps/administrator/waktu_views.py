from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import WaktuForm, DetailWaktuForm
from .models import Waktu, DetailWaktu, Hari


class WaktuIndexView(ListView):
    template_name = 'administrator/waktu/index.html'
    context = {
        'title_page': "Database | Waktu",
        'subtitle_page': "Halaman Database Waktu Pelajaran"
    }

    def get(self, request):
        all_detailwaktu = DetailWaktu.objects.all()
        self.context.update(
            {
                'all_detailwaktu': all_detailwaktu,
            }
        )
        return render(request, self.template_name, self.context)


class DetailWaktuCreateView(SuccessMessageMixin, CreateView):
    form_class = DetailWaktuForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Detail Waktu | Tambah',
        'subtitle_page': "Tambah Detail Waktu",
        'button': {
            'button_color': 'btn-success',
            'button_name': 'Tambah'
        },
        'back_url': 'administrator_IT:waktu_list'
    }
    success_url = reverse_lazy("administrator_IT:waktu_list")
    success_message = '%(hari)s  | %(waktu)s was created successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class DetailWaktuUpdateView(SuccessMessageMixin, UpdateView):
    model = DetailWaktu
    form_class = DetailWaktuForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Detail Waktu | Update',
        'subtitle_page': "Update Detail Waktu",
        'button': {
            'button_color': 'btn-warning',
            'button_name': 'Update'
        },
        'back_url': 'administrator_IT:waktu_list'
    }
    success_url = reverse_lazy("administrator_IT:waktu_list")
    success_message = '%(hari)s  | %(waktu)s was updated successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class DetailWaktuDeleteView(DeleteView):
    model = DetailWaktu
    template_name = 'administrator/delete_confirmation.html'
    success_url = reverse_lazy('administrator_IT:waktu_list')
    context_object_name = 'object_deleted'
    success_message = 'Data was deleted successfully'

    extra_context = {
        'title_page': 'Manage Detail Waktu | Delete',
        'subtitle_page': "Detail Waktu delete confirmation",
        'entity': 'Detail Waktu',
        'back_url': 'administrator_IT:waktu_list'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class WaktuCreateView(SuccessMessageMixin, CreateView):
    form_class = WaktuForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Waktu | Tambah',
        'subtitle_page': "Tambah Data Waktu",
        'button': {
            'button_color': 'btn-success',
            'button_name': 'Tambah'
        },
        'back_url': 'administrator_IT:waktu_list'
    }
    success_url = reverse_lazy("administrator_IT:waktu_list")
    success_message = '%(kode_waktu)s | %(nama_waktu)s was created successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class WaktuUpdateView(SuccessMessageMixin, UpdateView):
    model = Waktu
    form_class = WaktuForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Waktu | Update',
        'subtitle_page': "Update Data Waktu",
        'button': {
            'button_color': 'btn-warning',
            'button_name': 'Update'
        },
        'back_url': 'administrator_IT:waktu_list'
    }
    success_url = reverse_lazy("administrator_IT:waktu_list")
    success_message = '%(kode_waktu)s | %(nama_waktu)s was updated successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class WaktuDeleteView(DeleteView):
    model = Waktu
    template_name = 'administrator/delete_confirmation.html'
    success_url = reverse_lazy('administrator_IT:waktu_list')
    context_object_name = 'object_deleted'
    success_message = 'Data was deleted successfully'

    extra_context = {
        'title_page': 'Manage Waktu | Delete',
        'subtitle_page': "Waktu delete confirmation",
        'entity': 'Waktu',
        'back_url': 'administrator_IT:waktu_list'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
