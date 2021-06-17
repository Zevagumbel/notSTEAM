# Generated by Django 3.2.3 on 2021-06-11 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210610_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desarrollador',
            fields=[
                ('id_desarrollador', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del desarrollador')),
                ('nombre_desarrollador', models.CharField(max_length=128, verbose_name='nombre del desarrollador')),
            ],
        ),
        migrations.AlterField(
            model_name='juego',
            name='precio_juego',
            field=models.DateField(verbose_name='fecha de lanzamiento'),
        ),
    ]