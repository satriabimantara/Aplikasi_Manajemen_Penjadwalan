from django.contrib import admin
from django.urls import path, include
from .views import (
    IndexView,
    JadwalListView,
    loginView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView, name='login'),
    path('jadwal/', JadwalListView.as_view(), name='jadwal_list'),
    path('administrator/', include('administrator.urls', namespace='administrator_IT')),
    path('pimpinan/', include('pimpinan.urls', namespace='pimpinan')),
    path('tenagapengajar/', include('tenagapengajar.urls',
                                    namespace='tenagapengajar')),
    path('', IndexView.as_view(), name='index'),

]
# # add a flag for handling 404 page not found error
handler404 = 'aplikasi_manajemen_penjadwalan.views.error_404_view'
