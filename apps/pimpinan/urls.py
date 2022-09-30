from django.urls import path, include
from .views import (
    RevisiJadwalListView,
    RevisiJadwalUpdateView,
    RevisiJadwalDeleteView,
    RevisiJadwalCreateView
)

app_name = 'pimpinan'
urlpatterns = [
    path('revisi_jadwal/', RevisiJadwalListView.as_view(),
         name='revisi_jadwal_list'),
    path('revisi_jadwal/tambah/<int:pk>/', RevisiJadwalCreateView.as_view(),
         name='revisi_jadwal_create'),
    path('revisi_jadwal/update/<int:pk>/',
         RevisiJadwalUpdateView.as_view(), name='revisi_jadwal_update'),
    path('revisi_jadwal/delete/<int:pk>/',
         RevisiJadwalDeleteView.as_view(), name='revisi_jadwal_delete'),
]

# # add a flag for handling 404 page not found error
handler404 = 'aplikasi_manajemen_penjadwalan.views.error_404_view'
