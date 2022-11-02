# Generated by Django 2.2.16 on 2022-08-02 15:36

from django.db import migrations, models

import api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_auto_20220802_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, db_index=True, null=True, validators=[api.validators.validate_year], verbose_name='Год'),
        ),
    ]
