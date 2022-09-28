from django.urls import path, re_path
from django.views.generic import TemplateView

from .views import (
    IndexView,
    GuruListView,
    GuruCreateView,
    GuruUpdateView,
    GuruDeleteView,
    MataPelajaranIndexView,
    MataPelajaranCreateView,
    MataPelajaranUpdateView,
    MataPelajaranDeleteView,
    DetailMataPelajaranCreateView,
    DetailMataPelajaranUpdateView,
    DetailMataPelajaranDeleteView,
    RuanganListView,
    RuanganCreateView,
    RuanganUpdateView,
    RuanganDeleteView,
    DetailKelasCreateView,
    DetailKelasUpdateView,
    DetailKelasDeleteView,
    KelasIndexView,
    WaktuIndexView,
    WaktuCreateView,
    WaktuUpdateView,
    WaktuDeleteView,
    DetailWaktuCreateView,
    DetailWaktuUpdateView,
    DetailWaktuDeleteView,
    JadwalListView,
    JadwalCreateView,
    JadwalDeleteView,
    JadwalUpdateView,
    jadwal_reset
)

app_name = 'administrator_IT'
urlpatterns = [
    path('guru/', GuruListView.as_view(), name='guru_list'),
    path('guru/tambah/', GuruCreateView.as_view(), name='guru_create'),
    path('guru/update/<int:pk>/', GuruUpdateView.as_view(), name='guru_update'),
    path('guru/delete/<int:pk>/', GuruDeleteView.as_view(), name='guru_delete'),

    path('mata_pelajaran/', MataPelajaranIndexView.as_view(),
         name='mata_pelajaran_list'),
    path('mata_pelajaran/tambah/', MataPelajaranCreateView.as_view(),
         name='mata_pelajaran_create'),
    path('mata_pelajaran/update/<int:pk>/',
         MataPelajaranUpdateView.as_view(), name='mata_pelajaran_update'),
    path('mata_pelajaran/delete/<int:pk>/',
         MataPelajaranDeleteView.as_view(), name='mata_pelajaran_delete'),

    path('detail_mata_pelajaran/tambah/', DetailMataPelajaranCreateView.as_view(),
         name='detail_mata_pelajaran_create'),
    path('detail_mata_pelajaran/update/<int:pk>/',
         DetailMataPelajaranUpdateView.as_view(), name='detail_mata_pelajaran_update'),
    path('detail_mata_pelajaran/delete/<int:pk>/',
         DetailMataPelajaranDeleteView.as_view(), name='detail_mata_pelajaran_delete'),

    path('ruangan/', RuanganListView.as_view(), name='ruangan_list'),
    path('ruangan/tambah/', RuanganCreateView.as_view(), name='ruangan_create'),
    path('ruangan/update/<int:pk>/',
         RuanganUpdateView.as_view(), name='ruangan_update'),
    path('ruangan/delete/<int:pk>/',
         RuanganDeleteView.as_view(), name='ruangan_delete'),

    path('kelas/', KelasIndexView.as_view(), name='kelas_list'),
    path('kelas/tambah/', DetailKelasCreateView.as_view(), name='kelas_create'),
    path('kelas/update/<int:pk>/',
         DetailKelasUpdateView.as_view(), name='kelas_update'),
    path('kelas/delete/<int:pk>/',
         DetailKelasDeleteView.as_view(), name='kelas_delete'),

    path('waktu/', WaktuIndexView.as_view(),
         name='waktu_list'),
    path('waktu/tambah/', WaktuCreateView.as_view(),
         name='waktu_create'),
    path('waktu/update/<int:pk>/',
         WaktuUpdateView.as_view(), name='waktu_update'),
    path('waktu/delete/<int:pk>/',
         WaktuDeleteView.as_view(), name='waktu_delete'),

    path('detail_waktu/tambah/', DetailWaktuCreateView.as_view(),
         name='detail_waktu_create'),
    path('detail_waktu/update/<int:pk>/',
         DetailWaktuUpdateView.as_view(), name='detail_waktu_update'),
    path('detail_waktu/delete/<int:pk>/',
         DetailWaktuDeleteView.as_view(), name='detail_waktu_delete'),


    path('jadwal/', JadwalListView.as_view(), name='jadwal_list'),
    path('jadwal/reset/',
         jadwal_reset, name='jadwal_reset'),
    path('jadwal/tambah/', JadwalCreateView.as_view(), name='jadwal_create'),
    path('jadwal/update/<int:pk>/',
         JadwalUpdateView.as_view(), name='jadwal_update'),
    path('jadwal/delete/<int:pk>/',
         JadwalDeleteView.as_view(), name='jadwal_delete'),
    path('', IndexView.as_view(), name='index'),
]
# add a flag for handling 404 page not found error
handler404 = 'aplikasi_manajemen_penjadwalan.views.error_404_view'
