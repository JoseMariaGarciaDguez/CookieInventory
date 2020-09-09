# Generated by Django 2.1.7 on 2019-03-13 18:39

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_nombre', models.CharField(max_length=30)),
                ('categoria_descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_nombre', models.CharField(max_length=30)),
                ('producto_descripcion', models.CharField(max_length=200)),
                ('producto_stock', models.IntegerField()),
                ('producto_subfamilia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Categoria')),
            ],
        ),
    ]
