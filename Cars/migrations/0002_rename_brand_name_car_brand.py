# Generated by Django 5.0.3 on 2024-03-14 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='brand_name',
            new_name='brand',
        ),
    ]
