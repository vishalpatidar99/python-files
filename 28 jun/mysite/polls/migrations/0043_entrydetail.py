# Generated by Django 4.0.5 on 2022-07-08 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0042_other_some'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.entry')),
            ],
        ),
    ]