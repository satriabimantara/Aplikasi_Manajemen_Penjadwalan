from xml.dom import ValidationErr
from django import forms
from .models import Jadwal
from django.core.exceptions import ValidationError


class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = [
            'detail_pelajaran',
            'guru',
            'detail_waktu',
            'ruangan'
        ]
        widgets = {
            'detail_pelajaran': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'guru': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'detail_waktu': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'ruangan': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
        }

    def clean(self, *args, **kwargs):
        # method ini akan dipanggil sebelum is_valid() form dijalankan
        cleaned_data = super().clean(*args, **kwargs)
        detail_pelajaran = cleaned_data.get('detail_pelajaran')
        detail_waktu = cleaned_data.get('detail_waktu')
        guru = cleaned_data.get('guru')
        ruangan = cleaned_data.get('ruangan')
        print(detail_waktu)
        # check apakah data jadwal persis sudah ada di database?
        existing = Jadwal.objects.filter(
            detail_pelajaran=detail_pelajaran,
            detail_waktu=detail_waktu,
            guru=guru,
            ruangan=ruangan,
        ).exists()
        if existing:
            raise forms.ValidationError(
                'Schedule is already exist!', code='schedule_exist')
        # check apakah untuk di Waktu ke-X, kelas Y menerima lebih dari 1 mata pelajaran?
        existing_2 = Jadwal.objects.filter(
            detail_waktu=detail_waktu,
            detail_pelajaran__kelas_peserta__id=detail_pelajaran.kelas_peserta.id
        )
        if existing_2.exists():
            # check apakah mata pelajarannya sama? kalau sama berarti hanya update untuk field selain detail_pelajaran dan detail_waktu
            if existing_2[0].detail_pelajaran != detail_pelajaran:
                raise forms.ValidationError([
                    ValidationError(
                        'One class should only have one course in one time!', code='course_in_class_exist'),
                    ValidationError(
                        'Please check your input!', code='check_input')
                ])
            # else:
            #     # check kalau ruangannya berbeda maka raise error karena tidak mungkin 1 siswa berada di 2 tempat yang berbeda dalam waktu yang sama
            #     if existing_2[0].ruangan != ruangan:
            #         raise forms.ValidationError([
            #             ValidationError(
            #                 'One student should only have one course in one class room in one time!', code='course_in_class_exist'),
            #             ValidationError(
            #                 'Please check your input!', code='check_input')
            #         ])
        # check apakah untuk di Waktu ke-X, ruangan Y menerima lebih dari 1 mata pelajaran?
        existing_3 = Jadwal.objects.filter(
            detail_waktu=detail_waktu,
            ruangan=ruangan
        )
        if existing_3.exists():
            if existing_3[0].detail_pelajaran != detail_pelajaran:
                raise forms.ValidationError([
                    ValidationError(
                        'One class room should only have one course in one time!', code='room_in_class_exist'),
                    ValidationError(
                        'Please check your input!', code='check_input')
                ])
        # check apakah untuk di waktu ke-X, Guru Y mengajar lebih dari 1 mata pelajaran?
        existing_4 = Jadwal.objects.filter(
            detail_waktu=detail_waktu,
            guru=guru
        )
        if existing_4.exists():
            # check apakah mapel yang diajar Guru Y tidak berubah? kalau tidak berubah berarti hanya dilakukan update, sedangkan kalau berubah berarti munculkan error
            if existing_4[0].detail_pelajaran != detail_pelajaran:
                raise forms.ValidationError([
                    ValidationError(
                        'One teacher should only teach one course in one time!', code='teachers_in_one_time_exist'),
                    ValidationError(
                        'Please check your input!', code='check_input')
                ])
            # else:
            #     # check kalau ruangannya berbeda maka raise error karena tidak mungkin 1 guru berada di 2 tempat yang berbeda dalam waktu yang sama
            #     if existing_4[0].ruangan != ruangan:
            #         raise forms.ValidationError([
            #             ValidationError(
            #                 'One teacher should only teach one course in one class room in one time!', code='teach_in_another_room_in_one_time_exist'),
            #             ValidationError(
            #                 'Please check your input!', code='check_input')
            #         ])

        # check apakah jam pelajaran suatu mapel sudah melebihi batas?
        objects = Jadwal.objects.filter(
            detail_pelajaran=detail_pelajaran
        )
        if objects.exists():
            total_jam = objects[0].detail_pelajaran.total_jam
            daftar_kode_waktu = list()
            if total_jam == objects.count():
                # masukan daftar detail_waktu unique yang diperoleh dari hasil query
                for mapel in objects:
                    if mapel.detail_waktu not in daftar_kode_waktu:
                        daftar_kode_waktu.append(mapel.detail_waktu)
                # check apakah detail_waktu yang diinput user ada di daftar_kode_waktu? kalau iya maka hanya update data, selain itu munculkan warning
                if detail_waktu not in daftar_kode_waktu:
                    raise forms.ValidationError(
                        [
                            ValidationError(
                                'Maximum time schedule has been exceed!', code='maximum_time_schedule_exceed'),
                            ValidationError(
                                'Please check your input!', code='check_input')
                        ]
                    )
        return cleaned_data

    # def clean_detail_pelajaran(self):
    #     form_detail_pelajaran = self.cleaned_data.get('detail_pelajaran')
    #     existing = Jadwal.objects.filter(
    #         detail_pelajaran=form_detail_pelajaran)
    #     if existing:
    #         raise forms.ValidationError('Pelajaran Sudah Ada')
    #     return form_detail_pelajaran
