# Generated by Django 3.1.4 on 2021-07-14 07:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explore',
            name='img_link',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None),
        ),
    ]