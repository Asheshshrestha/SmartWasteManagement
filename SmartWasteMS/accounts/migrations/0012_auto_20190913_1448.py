# Generated by Django 2.2.2 on 2019-09-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190912_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6, null=True),
        ),
    ]
