# Generated by Django 2.0.1 on 2018-08-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20180823_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fmishortterm',
            name='weather_symbol_3',
            field=models.IntegerField(),
        ),
    ]