# Generated by Django 3.2.6 on 2021-09-10 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attende',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(default='C424', max_length=4, unique=True)),
                ('uid', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(999999999)])),
                ('purpose', models.CharField(max_length=12)),
                ('date', models.DateField(auto_now_add=True)),
                ('intime', models.TimeField(auto_now_add=True)),
                ('outtime', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]