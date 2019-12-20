# Generated by Django 2.2.2 on 2019-12-13 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bin', '0012_auto_20191028_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='dustbin',
            name='assigned_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
