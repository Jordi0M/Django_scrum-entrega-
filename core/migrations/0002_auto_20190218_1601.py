# Generated by Django 2.1.7 on 2019-02-18 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sprint',
            old_name='data_fnial',
            new_name='data_final',
        ),
    ]
