from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from .models import (
    Jadwal,
    Guru,
    MataPelajaran,
    DetailMataPelajaran,
    Kelas,
    DetailKelas,
    Waktu,
    DetailWaktu,
    Ruangan
)


class ResetIndexView(View):
    template_name = 'administrator/reset.html'
    context = {
        'title_page': "Reset Data",
        'subtitle_page': 'Halaman Reset Data'
    }

    def get(self, request, **params):
        data_reset_list = [
            'guru',
            'mata_pelajaran',
            'kelas_peserta',
            'ruangan',
            'waktu',
            'detail_mata_pelajaran',
            'detail_waktu',
            'jadwal'
        ]
        self.context.update({
            'data_reset_list': data_reset_list
        })

        return render(request, self.template_name, self.context)


template_reset_index = 'administrator/reset.html'


def guru_reset(request):
    context = {
        'title_page': 'Manage Guru | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetguru')
        if btn_reset == "reset":
            number_of_row_deleted = Guru.objects.all().delete()[0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Guru databases!'
                messages.warning(request, message)
            return redirect('administrator_IT:guru_list')
    return render(request, template_reset_index, context)


def kelas_peserta_reset(request):
    context = {
        'title_page': 'Manage Detail Kelas Peserta | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetkelas_peserta')
        if btn_reset == "reset":
            number_of_row_deleted = DetailKelas.objects.all().delete()[0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Detail kelas Peserta databases!'
                messages.warning(request, message)
            return redirect('administrator_IT:kelas_list')
    return render(request, template_reset_index, context)


def ruangan_reset(request):
    context = {
        'title_page': 'Manage Ruangan | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetruangan')
        if btn_reset == "reset":
            number_of_row_deleted = Ruangan.objects.all().delete()[0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Ruangan databases!'
                messages.warning(request, message)
            return redirect('administrator_IT:ruangan_list')
    return render(request, template_reset_index, context)


def mata_pelajaran_reset(request):
    context = {
        'title_page': 'Manage Mata Pelajaran | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetmata_pelajaran')
        if btn_reset == "reset":
            number_of_row_deleted = MataPelajaran.objects.all().delete()[0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Mata Pelajaran databases!'
                messages.warning(request, message)
            return redirect('administrator_IT:mata_pelajaran_list')
    return render(request, template_reset_index, context)


def waktu_reset(request):
    context = {
        'title_page': 'Manage Waktu | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetwaktu')
        if btn_reset == "reset":
            number_of_row_deleted = Waktu.objects.all().delete()[0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Waktu databases!'
                messages.warning(request, message)
            return redirect('administrator_IT:waktu_list')
    return render(request, template_reset_index, context)


def detail_mata_pelajaran_reset(request):
    context = {
        'title_page': 'Manage Detail Mata Pelajaran | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetdetail_mata_pelajaran')
        if btn_reset == "reset":
            number_of_row_deleted = DetailMataPelajaran.objects.all().delete()[
                0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Detail Mata Pelajaran databases!'
                messages.warning(request, message)
            return redirect('administrator_IT:detail_mata_pelajaran_list')
    return render(request, template_reset_index, context)


def detail_waktu_reset(request):
    context = {
        'title_page': 'Manage Detail Waktu | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetdetail_waktu')
        if btn_reset == "reset":
            number_of_row_deleted = DetailWaktu.objects.all().delete()[
                0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Detail Waktu databases!'
                messages.warning(request, message)
            return redirect('administrator_IT:waktu_list')
    return render(request, template_reset_index, context)


def jadwal_reset(request):
    context = {
        'title_page': 'Manage Jadwal | Reset',
    }
    if request.method == "POST":
        btn_reset = request.POST.get('btnResetjadwal')
        if btn_reset == "reset":
            number_of_row_deleted = Jadwal.objects.all().delete()[0]
            if number_of_row_deleted > 0:
                message = '{} records have been successfully deleted!'.format(
                    number_of_row_deleted)
                messages.success(request, message)
            else:
                message = 'There is not any rows in Schedule databases!'
                messages.warning(request, message)
            return redirect('jadwal_list')
    return render(request, template_reset_index, context)
