# Generated by Django 2.2.2 on 2019-10-07 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bin', '0009_auto_20191007_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='area_street',
        ),
        migrations.AddField(
            model_name='street',
            name='street_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bin.Area'),
        ),
        migrations.AlterField(
            model_name='dustbin',
            name='bin_street',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bin.street'),
        ),
    ]
