# Generated by Django 2.2.16 on 2022-08-02 15:25

import api.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Минимальная оценка - 1'), django.core.validators.MaxValueValidator(10, 'Максимальная оценка - 10')]),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[api.validators.validate_year], verbose_name='Год'),
        ),
    ]