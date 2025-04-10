from os import path
from sys import argv
from time import sleep
from datetime import datetime
from .db import *

DB_PATH = '%OneDrive%/Documents/Schule/SJ 2/SuD_SP/UnternehmensRechnungen.db' # TODO use param instead of hard coding
BASE_PATH = '/sys/bus/iio/devices/iio:device0'
PATH_TEMPERATURE = path.join(BASE_PATH, 'in_temp_input')
PATH_HUMIDITY = path.join(BASE_PATH, 'in_humidityrelative_input')
PATH_AIR_PRESSURE = path.join(BASE_PATH, 'in_pressure_input')

def get_data():
  """Reads the data from the device"""

  with (
    open(PATH_TEMPERATURE, mode='r', encoding='utf-8') as temperature_file
    , open(PATH_HUMIDITY, mode='r', encoding='utf-8') as humidity_file
    , open(PATH_AIR_PRESSURE, mode='r', encoding='utf-8') as air_pressure_file
  ):
    temperature = float(temperature_file.read())
    humidity = float(humidity_file.read())
    air_pressure = float(air_pressure_file.read())

  return temperature, humidity, air_pressure, datetime.now()

def format_data(temperature: float, humidity: float, air_pressure: float, timestamp: datetime) -> list[str]:
  """
  Returns a list of formatted data.
  :temperature float Temperature in celsius * 1000
  """

  temperature *= 0.001  # conversion
  humidity *= 0.001  # conversion
  air_pressure *= 10  # conversion

  return [
    f"========== {timestamp.isoformat(timespec='seconds').replace('T', '_ ')} =========="
    , f'Temperatur (Celsius): {temperature:.2f} °C'
    , f'Temperatur (Fahrenheit): {temperature * 1.8 + 32:.2f} F'
    , f'Luftfeuchte: {int(humidity)} % r.F.'
    , f'Luftdruck: {int(air_pressure)} hPa'
    , ''
  ]


def main(interval_sec=10, *data):
  """Run infinite loop with an interval"""

  if data: # support for test data
    formatted_data = format_data(*data)

  while True:
    data = get_data()
    formatted_data = format_data(*data)

    for line in formatted_data:
      print(line)

    sleep(interval_sec)


if __name__ == '__main__':
  main(*argv[1:]) # pylint: disable=too-many-function-args
