# Generated by Django 3.0.5 on 2020-04-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_num', '0002_auto_20200409_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='user_label',
            field=models.FloatField(blank=True, default=1, verbose_name='ユーザー識別'),
        ),
    ]
