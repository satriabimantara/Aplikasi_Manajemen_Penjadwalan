from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from .forms import (
    JadwalForm,
)
from .models import (
    Jadwal,
    DetailKelas,
    Hari,
    Waktu
)


class JadwalDeleteView(DeleteView):
    model = Jadwal
    template_name = 'administrator/delete_confirmation.html'
    success_url = reverse_lazy('database:jadwal_list')
    context_object_name = 'object_deleted'
    success_message = 'Data was deleted successfully'
    extra_context = {
        'title_page': 'Manage Jadwal | Delete',
        'subtitle_page': "Jadwal delete confirmation",
        'entity': 'Jadwal',
        'back_url': 'database:jadwal_list'
    }

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class JadwalListView(ListView):
    model = Jadwal
    template_name = "administrator/jadwal/list.html"
    context_object_name = 'jadwal_list'
    extra_context = {
        'title_page': 'Schedule | Lihat',
        'subtitle_page': "List Jadwal Pelajaran",
    }

    def get_queryset(self):
        # jadwal_list = dict()
        # days = Hari.objects.values_list('nama_hari', flat=True).distinct()
        # detail_kelas = DetailKelas.objects.values_list(
        #     'kode_kelas_peserta', flat=True).distinct().order_by('-kode_kelas_peserta')
        # for hari in days:
        #     jadwal_list[hari] = dict()
        #     for kelas in detail_kelas:
        #         jadwal_list[hari][kelas] = self.model.objects.filter(
        #             detail_waktu__hari__nama_hari__iexact=str(hari),
        #             detail_pelajaran__kelas_peserta__kode_kelas_peserta=str(
        #                 kelas)
        #         ).order_by('detail_waktu')
        # self.queryset = {
        #     'jadwal_list': jadwal_list,
        #     'days': days,
        # }
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


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
        'back_url': 'database:jadwal_list'
    }
    success_url = reverse_lazy("database:jadwal_list")
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
        'back_url': 'database:jadwal_list'
    }
    success_url = reverse_lazy("database:jadwal_list")
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


def jadwal_reset(request):
    context = {
        'title_page': 'Manage Jadwal | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetJadwal')
        if btn_reset == "reset":
            number_of_row_deleted = Jadwal.objects.all().delete()[0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Schedule databases!'
                messages.warning(request, message)
            return redirect('database:jadwal_list')
    return render(request, 'administrator/jadwal/list.html', context)
