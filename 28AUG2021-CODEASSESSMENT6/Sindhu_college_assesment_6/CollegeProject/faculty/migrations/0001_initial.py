# Generated by Django 3.2.6 on 2021-08-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobileno', models.BigIntegerField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
