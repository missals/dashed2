# Generated by Django 2.1 on 2018-08-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FMIShortTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_hour', models.DateTimeField()),
                ('geop_height', models.DecimalField(decimal_places=2, max_digits=9)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=9)),
                ('pressure', models.DecimalField(decimal_places=2, max_digits=9)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=9)),
                ('wind_direction', models.DecimalField(decimal_places=2, max_digits=9)),
                ('wind_speed_ms', models.DecimalField(decimal_places=2, max_digits=9)),
                ('wind_ums', models.DecimalField(decimal_places=2, max_digits=9)),
                ('wind_vms', models.DecimalField(decimal_places=2, max_digits=9)),
                ('maximum_wind', models.DecimalField(decimal_places=2, max_digits=9)),
                ('wind_gust', models.DecimalField(decimal_places=2, max_digits=9)),
                ('dew_point', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_cloud_cover', models.DecimalField(decimal_places=2, max_digits=9)),
                ('weather_symbol_3', models.DecimalField(decimal_places=2, max_digits=9)),
                ('low_cloud_cover', models.DecimalField(decimal_places=2, max_digits=9)),
                ('medium_cloud_cover', models.DecimalField(decimal_places=2, max_digits=9)),
                ('high_cloud_cover', models.DecimalField(decimal_places=2, max_digits=9)),
                ('precipitation_1h', models.DecimalField(decimal_places=2, max_digits=9)),
                ('precipitation_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('radiation_global_accumulation', models.DecimalField(decimal_places=2, max_digits=9)),
                ('radiation_lw_accumulation', models.DecimalField(decimal_places=2, max_digits=9)),
                ('radiation_net_surface_lw_accumulation', models.DecimalField(decimal_places=2, max_digits=9)),
                ('radiation_net_surface_sw_accumulation', models.DecimalField(decimal_places=2, max_digits=9)),
                ('radiation_diffuse_accumulation', models.DecimalField(decimal_places=2, max_digits=9)),
                ('land_sea_mask', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]