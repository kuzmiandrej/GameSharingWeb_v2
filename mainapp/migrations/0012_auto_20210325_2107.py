# Generated by Django 3.1.7 on 2021-03-25 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20210320_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='BagRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('slug', models.SlugField(unique=True)),
                ('rent', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Стоимость аренды')),
                ('cells', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Количество ячеек')),
                ('free_cells', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Количество свободных ячеек')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(blank=True, choices=[('booked', 'Игра забронирована'), ('passed check', 'Игра прошла проверку клиентом'), ('passed check employee', 'Игра прошла проверку сотрудником'), ('no passed check', 'Игра НЕ прошла проверку клиентом'), ('no passed check employee', 'Игра НЕ прошла проверку сотрудником'), ('start rent', 'Начало бронирования'), ('finish rent', 'Конец бронирования'), ('buy', 'Купили игру')], max_length=100, verbose_name='Тип события')),
                ('game_box', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.gamebox', verbose_name='Игра')),
            ],
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='category',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Notebook',
        ),
        migrations.DeleteModel(
            name='Smartphone',
        ),
        migrations.AddField(
            model_name='gamebox',
            name='bag_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.bagroom', verbose_name='Камера хранения'),
        ),
    ]
