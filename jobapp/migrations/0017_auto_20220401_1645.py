# Generated by Django 2.2 on 2022-04-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_auto_20220401_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_closed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
