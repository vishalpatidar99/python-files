# Generated by Django 4.0.5 on 2022-07-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0041_rename_date_dog_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Some',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
