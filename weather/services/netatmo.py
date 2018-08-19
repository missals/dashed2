import requests

from weather.local_settings import *

payload = {
    'grant_type': 'password',
    'username': NETATMO_USERNAME,
    'password': NETATMO_PASSWORD,
    'client_id': NETATMO_CLIENT_ID,
    'client_secret': NETATMO_CLIENT_SECRET,
    'scope': 'read_station'
}

device_id = NETATMO_MAIN_DEVICE_ID


class NetAtmoAPI:

    def __init__(self):

        self.access_token = None
        self.refresh_token = None
        self.expires_in = None

        self.authenticate()

    def authenticate(self):

        try:
            response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
            response.raise_for_status()
            access_token = response.json()["access_token"]
            refresh_token = response.json()["refresh_token"]
            expires_in = response.json()["expires_in"]
            scope = response.json()["scope"]
            print("Your access token is:", access_token)
            print("Your refresh token is:", refresh_token)
            print("Your scopes are:", scope)

        except requests.exceptions.HTTPError as error:
            print(error.response.status_code, error.response.text)
            return

        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in

    def get_user(self):

        params = {
            'access_token': self.access_token,
        }

        try:
            response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
            response.raise_for_status()
            data = response.json()["body"]

            return data

        except requests.exceptions.HTTPError as error:
            print(error.response.status_code, error.response.text)

            return None

    def get_stations_data(self):

        params = {
            'access_token': self.access_token,
            'device_id': device_id
        }

        try:
            response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
            response.raise_for_status()
            data = response.json()["body"]

            return data

        except requests.exceptions.HTTPError as error:
            print(error.response.status_code, error.response.text)

            return None


def get_example_user():

    example_response = {
        'devices': [
            {'_id': 'main_device_id',
             'cipher_id': 'some_weird_cipher_id',
             'date_setup': 1516125518,
             'last_setup': 1516125518,
             'type': 'NAMain',
             'last_status_store': 1534451298,
             'module_name': 'Living Room',
             'firmware': 134,
             'last_upgrade': 1516125520,
             'wifi_status': 37,
             'co2_calibrating': False,
             'station_name': 'Perttulantie',
             'data_type': ['Temperature', 'CO2', 'Humidity', 'Noise', 'Pressure'],
             'place': {
                 'altitude': 6,
                 'city': 'Helsinki',
                 'country': 'FI',
                 'timezone': 'Europe/Helsinki',
                 'location': [24, 60]
             },
             'dashboard_data': {
                 'time_utc': 1534451286,
                 'Temperature': 25.6,
                 'CO2': 429,
                 'Humidity': 47,
                 'Noise': 44,
                 'Pressure': 1024.4,
                 'AbsolutePressure': 1023.7,
                 'min_temp': 25.5,
                 'max_temp': 27.3,
                 'date_min_temp': 1534390762,
                 'date_max_temp': 1534440997,
                 'temp_trend': 'down',
                 'pressure_trend': 'stable'
             },
             'modules': [
                 {
                     '_id': 'balcony_device_id',
                     'type': 'NAModule1',
                     'module_name': 'Balcony',
                     'data_type': ['Temperature', 'Humidity'],
                     'last_setup': 1516125519,
                     'dashboard_data': {
                         'time_utc': 1534451246,
                         'Temperature': 21.8,
                         'Humidity': 58,
                         'min_temp': 17.6,
                         'max_temp': 27.7,
                         'date_min_temp': 1534387107,
                         'date_max_temp': 1534427661,
                         'temp_trend': 'stable'
                     },
                     'firmware': 46,
                     'last_message': 1534451297,
                     'last_seen': 1534451297,
                     'rf_status': 66,
                     'battery_vp': 5600,
                     'battery_percent': 83
                 },
                 {
                     '_id': 'bedroom_device_id',
                     'type': 'NAModule4',
                     'module_name': 'Bedroom',
                     'data_type': ['Temperature', 'CO2', 'Humidity'],
                     'last_setup': 1520184177,
                     'dashboard_data': {
                         'time_utc': 1534451239,
                         'Temperature': 24.2,
                         'CO2': 392,
                         'Humidity': 49,
                         'min_temp': 23.8,
                         'max_temp': 26,
                         'date_min_temp': 1534390433,
                         'date_max_temp': 1534437036,
                         'temp_trend': 'down'
                     },
                     'firmware': 44,
                     'last_message': 1534451297,
                     'last_seen': 1534451290,
                     'rf_status': 66,
                     'battery_vp': 5321,
                     'battery_percent': 62
                 }
             ]
             }
        ],
        'user': {
            'mail': 'me@gmail.com',
            'administrative': {
                'lang': 'en-US',
                'reg_locale': 'fi-FI',
                'unit': 0,
                'windunit': 2,
                'pressureunit': 0,
                'feel_like_algo': 1
            }
        }
    }

    return example_response


def get_example_station():

    example_response = {
                'devices': [
                    {
                        '_id': 'main_device_id',
                        'cipher_id': 'some_weird_cipher_id',
                        'date_setup': 1516125518, 'last_setup': 1516125518, 'type': 'NAMain',
                        'last_status_store': 1534451903, 'module_name': 'Living Room', 'firmware': 134,
                        'last_upgrade': 1516125520, 'wifi_status': 36, 'co2_calibrating': False,
                        'station_name': 'Main device name',
                        'data_type': ['Temperature', 'CO2', 'Humidity', 'Noise', 'Pressure'],
                        'place': {
                            'altitude': 6, 'city': 'Helsinki', 'country': 'FI',
                            'timezone': 'Europe/Helsinki', 'location': [24, 60]},
                        'dashboard_data': {
                            'time_utc': 1534451890, 'Temperature': 25.6, 'CO2': 418,
                            'Humidity': 47, 'Noise': 43, 'Pressure': 1024.4,
                            'AbsolutePressure': 1023.7, 'min_temp': 25.5,
                            'max_temp': 27.3, 'date_min_temp': 1534390762,
                            'date_max_temp': 1534440997, 'temp_trend': 'down',
                            'pressure_trend': 'stable'
                        },
                        'modules': [
                            {
                                '_id': 'balcony_device_id', 'type': 'NAModule1', 'module_name': 'Balcony',
                                'data_type': ['Temperature', 'Humidity'], 'last_setup': 1516125519,
                                'dashboard_data': {
                                    'time_utc': 1534451860, 'Temperature': 21.8, 'Humidity': 59,
                                    'min_temp': 17.6,
                                    'max_temp': 27.7, 'date_min_temp': 1534387107,
                                    'date_max_temp': 1534427661,
                                    'temp_trend': 'stable'
                                }, 'firmware': 46, 'last_message': 1534451898,
                                'last_seen': 1534451860, 'rf_status': 65, 'battery_vp': 5604, 'battery_percent': 84
                            },
                            {
                                '_id': 'bedroom_device_id', 'type': 'NAModule4', 'module_name': 'Bedroom',
                                'data_type': ['Temperature', 'CO2', 'Humidity'], 'last_setup': 1520184177,
                                'dashboard_data': {
                                    'time_utc': 1534451853, 'Temperature': 24.1, 'CO2': 401, 'Humidity': 50,
                                    'min_temp': 23.8, 'max_temp': 26, 'date_min_temp': 1534390433,
                                    'date_max_temp': 1534437036, 'temp_trend': 'stable'
                                },
                                'firmware': 44,
                                'last_message': 1534451898, 'last_seen': 1534451853, 'rf_status': 66, 'battery_vp': 5321,
                                'battery_percent': 62
                            }
                        ]
                    }
                ],
                'user': {
                    'mail': 'me@gmail.com',
                    'administrative': {
                        'lang': 'en-US',
                        'reg_locale': 'fi-FI',
                        'unit': 0, 'windunit': 2,
                        'pressureunit': 0,
                        'feel_like_algo': 1
                    }
                }
            }

    return example_response
