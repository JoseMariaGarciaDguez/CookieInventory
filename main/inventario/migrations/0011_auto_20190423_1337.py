# Generated by Django 2.2 on 2019-04-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_auto_20190423_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria_descripcion',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_descripcion',
            field=models.TextField(max_length=200),
        ),
    ]