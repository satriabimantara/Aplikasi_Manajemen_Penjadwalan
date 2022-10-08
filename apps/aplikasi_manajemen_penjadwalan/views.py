from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
)
from tenagapengajar.models import (
    Jadwal,
)
from administrator.models import (
    Hari
)


class IndexView(View):
    template_name = 'index.html'
    context = {
        'title_page': "Home",
        'subtitle_page': 'Halaman Home'
    }

    def get(self, request, **params):
        return render(request, self.template_name, self.context)


class JadwalListView(ListView):
    model = Jadwal
    template_name = "jadwal/list.html"
    context_object_name = 'jadwal_list'
    extra_context = {
        'title_page': 'Schedule | Lihat',
        'subtitle_page': "Daftar Jadwal Pelajaran",
    }

    def get_queryset(self):
        jadwal_list = dict()
        days = Hari.objects.values_list('nama_hari', flat=True).distinct()

        # Buat dictionary untuk setiap kelas di setiap hari
        for hari in days:
            jadwal_list[hari] = self.model.objects.filter(
                detail_waktu__hari__nama_hari__iexact=str(hari),
            ).order_by('detail_waktu')
        self.queryset = {
            'jadwal_list': jadwal_list,
            'days': days,
        }
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        # merge dictionary context yang sebelumnya dengan extra context
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


def loginView(request):
    context = {
        'title_page': 'LOGIN | Aplikasi Manajemen Penjadwalan'
    }

    # permission check untuk mengecek apakah user sudah login
    if request.method == "GET":
        if request.user.is_authenticated:
            # logika untuk user yang sudah login
            return redirect('index')
        else:
            # redirect user ke halaman login (belum login)
            return render(request, 'login.html', context)

    if request.method == "POST":
        # mengambil data user dari form login
        username_input = request.POST['username']
        password_input = request.POST['password']

        # authenticate untuk memastikan apakah user ini ada di dalam db atau tidak
        user = authenticate(
            request,
            username=username_input,
            password=password_input
        )
        if user is not None:
            # masukan data user ke dalam request
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')


def error_404_view(request, exception):
    return render(request, '404.html')
