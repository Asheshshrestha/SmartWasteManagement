# Generated by Django 2.2.2 on 2019-10-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bin', '0006_auto_20190911_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='dustbin',
            name='bin_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bin.Area'),
        ),
    ]