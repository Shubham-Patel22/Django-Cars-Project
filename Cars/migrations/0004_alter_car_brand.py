# Generated by Django 5.0.3 on 2024-03-15 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_alter_brand_brand_descr_alter_brand_brand_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Cars.brand'),
        ),
    ]