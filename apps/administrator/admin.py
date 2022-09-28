from django.contrib import admin
from django import forms
from .models import (
    Guru,
    MataPelajaran,
    DetailMataPelajaran,
    DetailKelas,
    Kelas,
    Jalur,
    Waktu,
    Hari,
    DetailWaktu,
    Ruangan,
    Jadwal,
    User,
    RoleUser,
    DetailUser
)
# Register your models here.


class DetailMataPelajaranForm(forms.ModelForm):
    kelas_peserta = forms.ModelChoiceField(
        queryset=DetailKelas.objects.order_by('kelas')
    )

    class Meta:
        model = DetailMataPelajaran
        fields = '__all__'

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        mapel = cleaned_data.get('mapel')
        kelas_peserta = cleaned_data.get('kelas_peserta')

        # check apakah sudah ada mapel dan kelas peserta yang sama di DB
        existing_same_mapel_and_kelas_peserta = DetailMataPelajaran.objects.filter(
            mapel=mapel,
            kelas_peserta=kelas_peserta
        ).exists()
        if existing_same_mapel_and_kelas_peserta:
            raise forms.ValidationError(
                'Mata Pelajaran dengan Kelas Peserta yang sama sudah ada!', code='mapel_kelas_exist')
        return cleaned_data


class DetailWaktuForm(forms.ModelForm):
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        hari = cleaned_data.get('hari')
        waktu = cleaned_data.get('waktu')

        # check apakah sudah ada hari dan waktu yang sama di DB
        existing_same_hari_dan_waktu = DetailWaktu.objects.filter(
            hari=hari,
            waktu=waktu
        ).exists()
        if existing_same_hari_dan_waktu:
            raise forms.ValidationError(
                'Hari dan Waktu yang sama sudah ada!', code='hari_waktu_exist')
        return cleaned_data


class DetailKelasForm(forms.ModelForm):
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        kelas = cleaned_data.get('kelas')
        jalur = cleaned_data.get('jalur')

        # check apakah sudah ada kelas dan jalur yang sama di DB
        existing_same_kelas_and_jalur = DetailKelas.objects.filter(
            kelas=kelas,
            jalur=jalur
        ).exists()
        if existing_same_kelas_and_jalur:
            raise forms.ValidationError(
                'Kelas dan Jalur yang sama sudah ada!', code='kelas_jalur_exist')
        return cleaned_data


class DetailKelasAdmin(admin.ModelAdmin):
    form = DetailKelasForm


class DetailMataPelajaranAdmin(admin.ModelAdmin):
    form = DetailMataPelajaranForm


class DetailWaktuAdmin(admin.ModelAdmin):
    form = DetailWaktuForm


admin.site.register(DetailMataPelajaran, DetailMataPelajaranAdmin)
admin.site.register(DetailKelas, DetailKelasAdmin)
admin.site.register(DetailWaktu, DetailWaktuAdmin)
admin.site.register([
    Guru,
    MataPelajaran,
    Jalur,
    Kelas,
    Waktu,
    Hari,
    Ruangan,
    Jadwal,
    User,
    RoleUser,
    DetailUser
])
