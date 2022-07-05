# Generated by Django 4.0.5 on 2022-07-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_moonlandings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='NAME', db_index=True, editable=False, max_length=35)),
                ('email', models.EmailField(db_column='EMAIL', db_index=True, db_tablespace=True, help_text='abc@gmail.com', max_length=35)),
            ],
        ),
    ]