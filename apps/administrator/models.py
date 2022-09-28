from django.db import models

# Create your models here.


class Guru(models.Model):
    nip = models.CharField(
        'Nomor Induk Pegawai',
        max_length=15,
        unique=True
    )
    nama_lengkap = models.CharField(
        'Nama Lengkap Guru',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        'Alamat Email Guru',
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['published']
        verbose_name_plural = "Guru"

    def __str__(self):
        return "{} - {}".format(self.nip, self.nama_lengkap)


class Jalur(models.Model):
    kode_jalur = models.CharField(
        'Kode Unik Jalur',
        max_length=5,
        unique=True
    )
    nama_jalur = models.CharField(
        'Nama Jalur',
        max_length=25,
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['published']
        verbose_name_plural = "Jalur"

    def __str__(self):
        return "{} - {}".format(self.kode_jalur, self.nama_jalur)


class Kelas(models.Model):
    CHOICES_KELAS = (
        ('Kelas X', 'Kelas X'),
        ('Kelas XI', 'Kelas XI'),
        ('Kelas XII', 'Kelas XII'),
    )

    nama_kelas = models.CharField(
        'Nama Kelas',
        choices=CHOICES_KELAS,
        max_length=12,
        unique=True
    )

    class Meta:
        ordering = ['nama_kelas']
        verbose_name_plural = "Kelas"

    def __str__(self):
        return self.nama_kelas


class Ruangan(models.Model):
    kode_ruangan = models.CharField(
        'Kode Ruangan (R01)',
        unique=True,
        max_length=10
    )
    nama_ruangan = models.CharField(
        'Nama Ruangan',
        unique=True,
        max_length=50
    )
    kapasitas_ruangan = models.PositiveSmallIntegerField(
        'Kapasitas Ruangan',
        blank=True,
        null=True
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['kode_ruangan']
        verbose_name_plural = "Ruangan"

    def __str__(self):
        return "{} - {} | {} peserta".format(
            self.kode_ruangan,
            self.nama_ruangan,
            self.kapasitas_ruangan
        )


class Waktu(models.Model):
    nama_waktu = models.CharField(
        'Rentang Waktu Pelajaran',
        max_length=30,
        unique=True
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Waktu"

    def __str__(self):
        return "{}".format(self.nama_waktu)


class Hari(models.Model):
    CHOICES_HARI = (
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('sabtu', 'Sabtu'),
    )
    nama_hari = models.CharField(
        'Nama Hari',
        choices=CHOICES_HARI,
        max_length=10,
        unique=True
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Hari"

    def __str__(self):
        return "{}".format(self.nama_hari.upper())


class MataPelajaran(models.Model):
    kode_mapel = models.CharField(
        'Kode Mata Pelajaran',
        max_length=10,
        unique=True
    )
    mapel = models.CharField(
        'Nama Mata Pelajaran',
        max_length=100,
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['kode_mapel']
        verbose_name_plural = "Mata Pelajaran"

    def __str__(self):
        return "{} - {}".format(self.kode_mapel, self.mapel)


class DetailWaktu(models.Model):
    hari = models.ForeignKey(
        Hari,
        on_delete=models.CASCADE
    )
    waktu = models.ForeignKey(
        Waktu,
        on_delete=models.CASCADE
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Detail Waktu"

    def __str__(self):
        return "{} | {} | {}".format(self.id, self.hari.nama_hari, self.waktu.nama_waktu)


class DetailKelas(models.Model):
    kelas = models.ForeignKey(
        Kelas,
        on_delete=models.CASCADE,
    )
    jalur = models.ForeignKey(
        Jalur,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Detail Kelas Peserta"

    def __str__(self):
        return "{} | Jalur-{}".format(
            self.kelas,
            self.jalur.nama_jalur
        )


class DetailMataPelajaran(models.Model):
    mapel = models.ForeignKey(
        MataPelajaran,
        on_delete=models.CASCADE
    )
    kelas_peserta = models.ForeignKey(
        DetailKelas,
        on_delete=models.CASCADE,
    )
    total_jam = models.PositiveSmallIntegerField(
        'Total Jam Pelajaran',
        blank=True,
        null=True
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Detail Mata Pelajaran"

    def __str__(self):
        return "{}. {} | {} - {}".format(
            self.id,
            self.mapel.mapel,
            self.kelas_peserta.kelas,
            self.kelas_peserta.jalur
        )


class Jadwal(models.Model):
    detail_pelajaran = models.ForeignKey(
        DetailMataPelajaran,
        on_delete=models.CASCADE
    )
    guru = models.ForeignKey(
        Guru,
        on_delete=models.CASCADE,
        default='- Belum Ada Pengajar -',
        blank=True,
        null=False
    )
    detail_waktu = models.ForeignKey(
        DetailWaktu,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    ruangan = models.ForeignKey(
        Ruangan,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    CHOICE_STATUS_VALIDASI = (
        ('Unlock', 'Unlock'),
        ('Lock', 'Lock'),
    )
    status_validasi = models.CharField(
        'Status Validasi Jadwal',
        choices=CHOICE_STATUS_VALIDASI,
        default=CHOICE_STATUS_VALIDASI[0][1],
        max_length=10,
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['published']
        verbose_name_plural = "Jadwal"

    def __str__(self):
        final_string = "{}. {} - {} - {} - {} | ".format(
            self.id,
            self.detail_pelajaran.mapel.mapel,
            self.guru.nama_lengkap,
            self.detail_pelajaran.kelas_peserta.kelas,
            self.detail_pelajaran.kelas_peserta.jalur.nama_jalur
        )
        # cek apakah waktu None?
        if self.detail_waktu == None:
            extra_string = "-- WITA | "
        else:
            extra_string = "{}: {} | ".format(
                self.detail_waktu.hari.nama_hari,
                self.detail_waktu.waktu.nama_waktu
            )
        final_string += extra_string
        # cek apakah ruangan None?
        if self.ruangan == None:
            extra_string = "- ruang | "
        else:
            extra_string = "{}".format(
                self.ruangan.nama_ruangan,
            )
        final_string += extra_string
        return final_string


class User(models.Model):
    kode_user = models.CharField(
        'NIP atau Nomor Induk Siswa',
        max_length=20,
        unique=True
    )
    nama_lengkap = models.CharField(
        'Nama Lengkap User',
        max_length=150,
        unique=True
    )
    email = models.EmailField('Alamat Email User')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['kode_user']
        verbose_name_plural = "User"

    def __str__(self):
        return "{}. {} | {}".format(self.id, self.nama_lengkap, self.username)


class RoleUser(models.Model):
    CHOICE_ROLE_USER = (
        ('Administrator', 'Administrator'),
        ('Pimpinan', 'Pimpinan'),
        ('TenagaPengajar', 'TenagaPengajar'),
        ('Siswa', 'Siswa'),
    )
    nama_role = models.CharField(
        'Role Pengguna',
        choices=CHOICE_ROLE_USER,
        unique=True,
        max_length=20
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['nama_role']
        verbose_name_plural = "Role User"

    def __str__(self):
        return self.nama_role


class DetailUser(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    role_user = models.ForeignKey(
        RoleUser,
        on_delete=models.CASCADE
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Detail User"

    def __str__(self):
        return "{}. {} - {}".format(self.id, self.user.nama_lengkap, self.role_user.nama_role)
