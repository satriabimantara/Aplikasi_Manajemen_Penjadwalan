from django.contrib import admin
from django.urls import path, include
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('administrator/', include('administrator.urls', namespace='administrator_IT'))
]
# # add a flag for handling 404 page not found error
handler404 = 'aplikasi_manajemen_penjadwalan.views.error_404_view'
