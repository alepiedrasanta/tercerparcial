# Generated by Django 3.2.9 on 2021-11-11 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200)),
                ('detalles', models.CharField(max_length=500)),
                ('precio', models.CharField(max_length=500)),
            ],
        ),
    ]
