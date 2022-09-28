from django.shortcuts import render
from django.views import View
from .guru_views import (
    GuruCreateView,
    GuruDeleteView,
    GuruUpdateView,
    GuruListView
)
from .mapel_views import (
    MataPelajaranCreateView,
    MataPelajaranDeleteView,
    MataPelajaranUpdateView,
    MataPelajaranIndexView,
    DetailMataPelajaranCreateView,
    DetailMataPelajaranDeleteView,
    DetailMataPelajaranUpdateView,
)
from .ruangan_views import (
    RuanganCreateView,
    RuanganDeleteView,
    RuanganUpdateView,
    RuanganListView
)
from .kelas_views import (
    DetailKelasCreateView,
    DetailKelasDeleteView,
    DetailKelasUpdateView,
    KelasIndexView
)

from .waktu_views import (
    WaktuIndexView,
    WaktuCreateView,
    WaktuUpdateView,
    WaktuDeleteView,
    DetailWaktuCreateView,
    DetailWaktuUpdateView,
    DetailWaktuDeleteView
)
from .jadwal_views import (
    JadwalListView,
    JadwalCreateView,
    JadwalDeleteView,
    JadwalUpdateView,
    jadwal_reset
)
from .models import (
    DetailWaktu,
    Guru,
    MataPelajaran,
    DetailMataPelajaran,
    DetailKelas,
    Waktu,
    Ruangan,
)


class IndexView(View):
    template_name = 'administrator/index.html'
    context = {
        'title_page': "Administrator Dashboard",
        'subtitle_page': "Halaman Administrator"
    }

    def get(self, request):
        count_mapel = MataPelajaran.objects.count()
        count_detail_mapel = DetailMataPelajaran.objects.count()
        count_guru = Guru.objects.count()
        count_ruangan = Ruangan.objects.count()
        count_kelas_peserta = DetailKelas.objects.count()
        count_waktu = Waktu.objects.count()
        count_detail_waktu = DetailWaktu.objects.count()
        self.context.update(
            {
                'count_mapel': count_mapel,
                'count_detail_mapel': count_detail_mapel,
                'count_guru': count_guru,
                'count_ruangan': count_ruangan,
                'count_kelas_peserta': count_kelas_peserta,
                'count_waktu': count_waktu,
                'count_detail_waktu': count_detail_waktu,
            }
        )
        return render(request, self.template_name, self.context)
