import requests
import xml.etree.ElementTree as ET

from dateutil.parser import parse

from weather.local_settings import FMI_APIKEY, FMI_PLACE
from weather.models import FMIShortTerm

from dashed.settings import TIME_ZONE

apikey = FMI_APIKEY
place = FMI_PLACE

query = 'fmi::forecast::hirlam::surface::point::timevaluepair'
# query = 'fmi::forecast::harmonie::surface::point::timevaluepair'

var_tag = '{http://www.opengis.net/gml/3.2}id'
ts_tag = '{http://www.opengis.net/waterml/2.0}MeasurementTimeseries'
time_tag = '{http://www.opengis.net/waterml/2.0}time'
value_tag = '{http://www.opengis.net/waterml/2.0}value'

url = 'http://data.fmi.fi/fmi-apikey/{}/wfs?request=getFeature&storedquery_id={}&place={}'.format(
    apikey, query, place
)


def refresh_data():
    req = requests.get(url)
    datatree = ET.ElementTree(ET.fromstring(req.content))
    variables = [ts.attrib.get(var_tag) for ts in datatree.iter(ts_tag)]

    data = []

    series = [s for s in datatree.iter(ts_tag)]

    first_times = [t.text for t in series[0].iter(time_tag)]

    for t in series[0].iter(time_tag):
        data.append({'time': t.text})

    for series, variable in zip(series, variables):

        times = [t.text for t in series.iter(time_tag)]

        if times != first_times:
            print("Timestamps are not the same for each series!")

        values = [v.text for v in series.iter(value_tag)]

        for d, value in zip(data, values):
            d[variable] = value

    objs = []

    for d in data:
        obj = FMIShortTerm(
            event_hour=d['time'],
            geop_height=d['mts-1-1-GeopHeight'],
            temperature=d['mts-1-1-Temperature'],
            pressure=d['mts-1-1-Pressure'],
            humidity=d['mts-1-1-Humidity'],
            wind_direction=d['mts-1-1-WindDirection'],
            wind_speed_ms=d['mts-1-1-WindSpeedMS'],
            wind_ums=d['mts-1-1-WindUMS'],
            wind_vms=d['mts-1-1-WindVMS'],
            maximum_wind=d['mts-1-1-MaximumWind'],
            wind_gust=d['mts-1-1-WindGust'],
            dew_point=d['mts-1-1-DewPoint'],
            total_cloud_cover=d['mts-1-1-TotalCloudCover'],
            weather_symbol_3=int(float(d['mts-1-1-WeatherSymbol3'])),
            low_cloud_cover=d['mts-1-1-LowCloudCover'],
            medium_cloud_cover=d['mts-1-1-MediumCloudCover'],
            high_cloud_cover=d['mts-1-1-HighCloudCover'],
            precipitation_1h=d['mts-1-1-Precipitation1h'],
            precipitation_amount=d['mts-1-1-PrecipitationAmount'],
            radiation_global_accumulation=d['mts-1-1-RadiationGlobalAccumulation'],
            radiation_lw_accumulation=d['mts-1-1-RadiationLWAccumulation'],
            radiation_net_surface_lw_accumulation=d['mts-1-1-RadiationNetSurfaceLWAccumulation'],
            radiation_net_surface_sw_accumulation=d['mts-1-1-RadiationNetSurfaceSWAccumulation'],
            radiation_diffuse_accumulation=d['mts-1-1-RadiationDiffuseAccumulation'],
            land_sea_mask=d['mts-1-1-LandSeaMask'],
        )
        objs.append(obj)

    FMIShortTerm.objects.all().delete()
    FMIShortTerm.objects.bulk_create(objs)

    return data, objs, datatree
