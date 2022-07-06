# Generated by Django 4.0.5 on 2022-07-06 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_alter_practice_n'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date_of_manufacturing', models.DateField()),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.manufacturer')),
            ],
        ),
    ]
