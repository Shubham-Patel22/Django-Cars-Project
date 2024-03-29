# Generated by Django 5.0.3 on 2024-03-13 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('brand_descr', models.TextField()),
                ('brand_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('top_speed', models.IntegerField()),
                ('mileage', models.FloatField()),
                ('cost', models.IntegerField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cars.brand')),
            ],
        ),
    ]
