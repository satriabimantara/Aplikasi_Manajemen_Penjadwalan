# Generated by Django 4.1.1 on 2022-09-30 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_delete_revisijadwal'),
        ('pimpinan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revisijadwal',
            name='id',
        ),
        migrations.AlterField(
            model_name='revisijadwal',
            name='jadwal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='administrator.jadwal'),
        ),
    ]
