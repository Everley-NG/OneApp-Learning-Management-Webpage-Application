# Generated by Django 3.1.7 on 2021-04-13 18:51

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=app.models.ListField(verbose_name=app.models.ListField()),
        ),
    ]
