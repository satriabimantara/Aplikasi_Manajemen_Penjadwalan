from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import GuruForms
from .models import Guru


class GuruListView(ListView):
    model = Guru
    template_name = "administrator/guru/list.html"
    context_object_name = 'guru_list'
    extra_context = {
        'title_page': 'Database | Guru',
        'subtitle_page': "Daftar Guru",
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class GuruCreateView(SuccessMessageMixin, CreateView):
    form_class = GuruForms
    template_name = 'create.html'
    extra_context = {
        'title_page': 'Manage Guru | Tambah',
        'subtitle_page': "Tambah Data Guru",
        'button': {
            'button_color': 'btn-success',
            'button_name': 'Tambah'
        },
        'back_url': 'administrator_IT:guru_list'
    }
    success_url = reverse_lazy("administrator_IT:guru_create")
    success_message = '%(nip)s | %(nama_lengkap)s was created successfully'

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


class GuruUpdateView(SuccessMessageMixin, UpdateView):
    model = Guru
    form_class = GuruForms
    template_name = 'create.html'
    extra_context = {
        'title_page': 'Manage Guru | Update',
        'subtitle_page': "Update Guru",
        'button': {
            'button_color': 'btn-warning',
            'button_name': 'Update'
        },
        'back_url': 'administrator_IT:guru_list'
    }
    success_url = reverse_lazy("administrator_IT:guru_list")
    success_message = '%(nip)s | %(nama_lengkap)s was updated successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class GuruDeleteView(DeleteView):
    model = Guru
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('administrator_IT:guru_list')
    context_object_name = 'object_deleted'
    success_message = 'Data was deleted successfully'
    extra_context = {
        'title_page': 'Manage Guru | Delete',
        'subtitle_page': "Guru delete confirmation",
        'entity': 'Guru',
        'back_url': 'administrator_IT:guru_list'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
