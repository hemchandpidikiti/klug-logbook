# Generated by Django 3.2.6 on 2021-09-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0004_auto_20210910_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attende',
            name='intime',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='attende',
            name='outtime',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]