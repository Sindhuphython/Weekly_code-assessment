# Generated by Django 3.2.6 on 2021-08-21 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='addess',
            new_name='address',
        ),
    ]
