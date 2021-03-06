# Generated by Django 4.0.3 on 2022-04-10 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=30, verbose_name='Устройство')),
                ('series', models.CharField(max_length=30, verbose_name='Серия')),
                ('memory', models.CharField(max_length=30, verbose_name='Память')),
                ('cost', models.CharField(max_length=30, verbose_name='Цена')),
                ('color', models.CharField(max_length=30, verbose_name='Цвет')),
                ('region', models.CharField(max_length=30, verbose_name='Регион')),
                ('extra', models.CharField(max_length=255, verbose_name='Исходная строка')),
                ('new_line', models.CharField(max_length=255, verbose_name='Строка состояния')),
                ('provider', models.CharField(max_length=25, verbose_name='Поставщик')),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Цены | Поиск',
                'verbose_name_plural': 'Цены | Поиск',
            },
        ),
        migrations.CreateModel(
            name='ProviderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщик',
            },
        ),
        migrations.CreateModel(
            name='NewPriceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.TextField(verbose_name='Новый прайс')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Поставщик', to='cost_models.providermodel')),
            ],
            options={
                'verbose_name': 'Новый прайс | Управление cvs файлом',
                'verbose_name_plural': 'Новый прайс | Управление cvs файлом',
            },
        ),
    ]
