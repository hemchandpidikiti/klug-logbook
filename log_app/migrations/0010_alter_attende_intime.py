# Generated by Django 3.2.6 on 2021-09-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0009_alter_attende_intime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attende',
            name='intime',
            field=models.TimeField(auto_now_add=True),
        ),
    ]