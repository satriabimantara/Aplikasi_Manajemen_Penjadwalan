# Generated by Django 4.1.1 on 2022-09-30 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pimpinan', '0003_alter_revisijadwal_jadwal'),
        ('administrator', '0004_remove_jadwal_detail_pelajaran_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Jadwal',
        ),
    ]