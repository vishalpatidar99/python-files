# Generated by Django 4.0.5 on 2022-07-04 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_studentnew1_alter_studentnew_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentnew1',
            options={'managed': False, 'ordering': ['name']},
        ),
    ]