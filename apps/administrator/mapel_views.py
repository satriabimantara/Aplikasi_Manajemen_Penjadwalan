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
from .forms import MataPelajaranForms, DetailMataPelajaranForm
from .models import MataPelajaran, DetailMataPelajaran


class MataPelajaranIndexView(ListView):
    template_name = 'administrator/mapel/index.html'
    context = {
        'title_page': "Database | Mata Pelajaran",
        'subtitle_page': "Halaman Database Mata Pelajaran"
    }

    def get(self, request):
        all_mapel = MataPelajaran.objects.all()
        all_detailmapel = DetailMataPelajaran.objects.all()
        self.context.update(
            {
                'all_mapel': all_mapel,
                'all_detailmapel': all_detailmapel,
            }
        )
        return render(request, self.template_name, self.context)


class DetailMataPelajaranCreateView(SuccessMessageMixin, CreateView):
    form_class = DetailMataPelajaranForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Detail Mapel | Tambah',
        'subtitle_page': "Tambah Detail Mata Pelajaran",
        'button': {
            'button_color': 'btn-success',
            'button_name': 'Tambah'
        },
        'back_url': 'administrator_IT:mata_pelajaran_list'
    }
    success_url = reverse_lazy("administrator_IT:mata_pelajaran_list")
    success_message = '%(mapel)s  | %(kelas_peserta)s was created successfully'

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


class DetailMataPelajaranUpdateView(SuccessMessageMixin, UpdateView):
    model = DetailMataPelajaran
    form_class = DetailMataPelajaranForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Detail Mapel | Update',
        'subtitle_page': "Update Detail Mata Pelajaran",
        'button': {
            'button_color': 'btn-warning',
            'button_name': 'Update'
        },
        'back_url': 'administrator_IT:mata_pelajaran_list'
    }
    success_url = reverse_lazy("administrator_IT:mata_pelajaran_list")
    success_message = '%(kode_detailmapel)s | %(mapel)s  | %(kelas_peserta)s was updated successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class DetailMataPelajaranDeleteView(DeleteView):
    model = DetailMataPelajaran
    template_name = 'administrator/delete_confirmation.html'
    success_url = reverse_lazy('administrator_IT:mata_pelajaran_list')
    context_object_name = 'object_deleted'
    success_message = 'Data was deleted successfully'

    extra_context = {
        'title_page': 'Manage Detail Mapel | Delete',
        'subtitle_page': "Detail Mata Pelajaran delete confirmation",
        'entity': 'Detail Mata Pelajaran',
        'back_url': 'administrator_IT:mata_pelajaran_list'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class MataPelajaranCreateView(SuccessMessageMixin, CreateView):
    form_class = MataPelajaranForms
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Mapel | Tambah',
        'subtitle_page': "Tambah Data Mata Pelajaran",
        'button': {
            'button_color': 'btn-success',
            'button_name': 'Tambah'
        },
        'back_url': 'administrator_IT:mata_pelajaran_list'
    }
    success_url = reverse_lazy("administrator_IT:mata_pelajaran_list")
    success_message = '%(kode_mapel)s | %(mapel)s was created successfully'

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


class MataPelajaranUpdateView(SuccessMessageMixin, UpdateView):
    model = MataPelajaran
    form_class = MataPelajaranForms
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Mapel | Update',
        'subtitle_page': "Update Data Mata Pelajaran",
        'button': {
            'button_color': 'btn-warning',
            'button_name': 'Update'
        },
        'back_url': 'administrator_IT:mata_pelajaran_list'
    }
    success_url = reverse_lazy("administrator_IT:mata_pelajaran_list")
    success_message = '%(kode_mapel)s | %(mapel)s was updated successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class MataPelajaranDeleteView(DeleteView):
    model = MataPelajaran
    template_name = 'administrator/delete_confirmation.html'
    success_url = reverse_lazy('administrator_IT:mata_pelajaran_list')
    context_object_name = 'object_deleted'
    success_message = 'Data was deleted successfully'

    extra_context = {
        'title_page': 'Manage Mapel | Delete',
        'subtitle_page': "Mata Pelajaran delete confirmation",
        'entity': 'Mata Pelajaran',
        'back_url': 'administrator_IT:mata_pelajaran_list'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)