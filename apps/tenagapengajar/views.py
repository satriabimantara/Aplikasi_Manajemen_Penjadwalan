from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from administrator.forms import (
    JadwalForm,
)
from administrator.models import (
    Jadwal,
)
# Create your views here.


class JadwalCreateView(SuccessMessageMixin, CreateView):
    form_class = JadwalForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Jadwal | Tambah',
        'subtitle_page': "Tambah Data Jadwal",
        'button': {
            'button_color': 'btn-success',
            'button_name': 'Tambah'
        },
        'back_url': 'jadwal_list'
    }
    success_url = reverse_lazy("jadwal_list")
    success_message = '%(detail_pelajaran)s | %(guru)s | %(detail_waktu)s was created successfully'

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


class JadwalUpdateView(SuccessMessageMixin, UpdateView):
    model = Jadwal
    form_class = JadwalForm
    template_name = 'administrator/create.html'
    extra_context = {
        'title_page': 'Manage Jadwal | Update',
        'subtitle_page': "Update Jadwal",
        'button': {
            'button_color': 'btn-warning',
            'button_name': 'Update'
        },
        'back_url': 'jadwal_list'
    }
    success_url = reverse_lazy("jadwal_list")
    success_message = '%(detail_pelajaran)s | %(guru)s | %(detail_waktu)s was updated successfully'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class JadwalDeleteView(DeleteView):
    model = Jadwal
    template_name = 'administrator/delete_confirmation.html'
    success_url = reverse_lazy('jadwal_list')
    context_object_name = 'object_deleted'
    success_message = 'Data was deleted successfully'
    extra_context = {
        'title_page': 'Manage Jadwal | Delete',
        'subtitle_page': "Jadwal delete confirmation",
        'entity': 'Jadwal',
        'back_url': 'jadwal_list'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
