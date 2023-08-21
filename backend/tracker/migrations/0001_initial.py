# Generated by Django 4.2.4 on 2023-08-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='site/logo/')),
            ],
            options={
                'verbose_name': 'site',
                'verbose_name_plural': '1. Site',
            },
        ),
    ]
