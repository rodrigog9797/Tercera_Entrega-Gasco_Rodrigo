# Generated by Django 5.1.3 on 2024-11-25 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppGasco', '0002_rename_descripcion_categoria_descripcion_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]
