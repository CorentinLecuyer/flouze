# Generated by Django 4.2.4 on 2023-08-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbrevation', models.CharField(max_length=2)),
                ('language', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': '1. Countries',
            },
        ),
    ]