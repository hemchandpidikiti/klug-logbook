# Generated by Django 3.2.6 on 2021-09-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0014_alter_attende_date_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attende',
            name='date_out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]