# Generated by Django 2.2.3 on 2019-08-01 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0005_auto_20190801_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservabr',
            name='hotel',
        ),
        migrations.AddField(
            model_name='reservabr',
            name='restbar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ReservaBR', to='reserva.RestBar'),
            preserve_default=False,
        ),
    ]