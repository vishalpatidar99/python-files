# Generated by Django 4.0.5 on 2022-07-04 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_alter_studentnew2_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentnew2',
            options={'managed': False, 'ordering': ['name']},
        ),
    ]
