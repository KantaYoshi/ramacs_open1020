# Generated by Django 3.0.5 on 2020-04-09 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_num', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
