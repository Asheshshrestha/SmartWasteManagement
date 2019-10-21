# Generated by Django 2.2.2 on 2019-10-14 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='notice_for_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('message', models.TextField()),
                ('notice_to', models.CharField(choices=[('1', 'all'), ('2', 'Admin'), ('2', 'Staff')], max_length=5)),
                ('notice_date', models.DateField()),
                ('notice_time', models.TimeField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
