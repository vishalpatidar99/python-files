# Generated by Django 4.0.5 on 2022-07-25 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls2', '0011_alter_book5_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='resume',
        ),
    ]