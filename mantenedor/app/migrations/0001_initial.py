# Generated by Django 2.1.1 on 2019-10-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=250)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]