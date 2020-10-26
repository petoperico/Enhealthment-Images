# Generated by Django 3.1.2 on 2020-10-25 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nombre')),
                ('image', models.ImageField(upload_to='original_images')),
            ],
            options={
                'verbose_name': 'Imagen Original',
                'verbose_name_plural': 'Imagenes Originales',
            },
        ),
        migrations.CreateModel(
            name='EnhancementImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=50, verbose_name='metodo')),
                ('image', models.ImageField(upload_to='enhancement_images')),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enhancements', to='images.originalimage', verbose_name='imagen original')),
            ],
            options={
                'verbose_name': 'Imagen Mejorada',
                'verbose_name_plural': 'Imagenes Mejoradas',
            },
        ),
    ]
