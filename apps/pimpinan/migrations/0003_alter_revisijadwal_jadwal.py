# Generated by Django 4.1.1 on 2022-09-30 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenagapengajar', '0001_initial'),
        ('pimpinan', '0002_remove_revisijadwal_id_alter_revisijadwal_jadwal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisijadwal',
            name='jadwal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tenagapengajar.jadwal'),
        ),
    ]
