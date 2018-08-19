import requests
import xml.etree.ElementTree as ET

from weather.local_settings import *

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


def get_data():
    req = requests.get(url)
    datatree = ET.ElementTree(ET.fromstring(req.content))
    variables = [ts.attrib.get(var_tag) for ts in datatree.iter(ts_tag)]

    print(variables)

    data = []

    series = [s for s in datatree.iter(ts_tag)]

    first_times = [t.text for t in series[0].iter(time_tag)]

    for t in series[0].iter(time_tag):
        data.append({'time': t.text})

    for series, variable in zip(series, variables):

        print(variable)

        times = [t.text for t in series.iter(time_tag)]

        if times != first_times:
            print("Timestamps are not the same for each series!")

        values = [v.text for v in series.iter(value_tag)]

        for d, value in zip(data, values):
            d[variable] = value

    for d in data:
        print("{}: {}".format(d['time'], d['mts-1-1-Temperature']))

    return data
