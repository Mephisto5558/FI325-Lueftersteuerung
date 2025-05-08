from os import path
from sys import argv
from time import sleep
from datetime import datetime
from math import exp, log

from .csv_handler import save_to_csv

CSV_FILEPATH = '../logs/data.csv'
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
    temperature = temperature_file.read()
    humidity = humidity_file.read()
    air_pressure = air_pressure_file.read()

    temperature = None if temperature is None else float(temperature)
    humidity = None if humidity is None else float(humidity)
    air_pressure = None if air_pressure is None else float(temperature)

  return temperature, humidity, air_pressure, datetime.now()

def calc_data(temperature: float, humidity: float, air_pressure: float, timestamp: datetime):
  """Calculate the values."""

  if None in (temperature, humidity, air_pressure, timestamp):
    raise TypeError(
        f'Missing data from device {BASE_PATH}', f'{temperature=}, {humidity=}, {air_pressure=}, {timestamp=}'
    )

  temperature_c = round(temperature * 0.001, 2)
  temperature_f = round(temperature * 0.001 * 1.8 + 32, 2)
  humidity = int(humidity * 0.001)
  air_pressure = int(air_pressure * 10)

  # https://www.messpc.de/messpc_formeleditor.php
  dew_point_pt1 = log(
      6.1
      * exp((7.45 * temperature) / (234.67 + temperature) * 2.3025851)
      * humidity / 100 / 6.1
  )

  dew_point = (
      (234.67 * 0.434292289 * dew_point_pt1)
      / (7.45 - 0.434292289 * dew_point_pt1)
  )

  dew_point_c = round(dew_point, 2)
  dew_point_f = round(dew_point * 1.8 + 32, 2)

  return temperature_c, temperature_f, humidity, air_pressure, dew_point_c, dew_point_f, timestamp

def format_data(
    temperature_c: float, temperature_f: float,
    humidity: int, air_pressure: int, dew_point_c: float, dew_point_f: float, timestamp: datetime
) -> list[str]:
  """Returns a list of formatted data."""

  return [
      f"========== {timestamp.isoformat(timespec='seconds').replace('T', '_ ')} ==========",
      f'Temperatur (Celsius): {temperature_c} °C',
      f'Temperatur (Fahrenheit): {temperature_f} F',
      f'Taupunkt (Celsius): {dew_point_c} °C',
      f'Taupunkt (Farenheit): {dew_point_f} F',
      f'Luftfeuchte: {humidity} % r.F.',
      f'Luftdruck: {air_pressure} hPa',
      '']

def main(interval_sec=10):
  """Run infinite loop with an interval"""

  if not path.exists(BASE_PATH):
    # the device was possibly not initialised
    raise FileNotFoundError(
        f'Missing device {BASE_PATH=}'
        + '\n\tThe device needs to be initialized by running'
        + '\n\t`i2cdetect -y 1 and`'
        + '\n\t`echo "bme280 0x77" > /sys/bus/i2c/devices/i2c-1/new_device` in a root shell.'
    )

  with open(CSV_FILEPATH, mode='r', encoding='utf-8') as csv_file:
    while True:
      data = calc_data(*get_data())
      save_to_csv(csv_file, *data)

      formatted_data = format_data(*data)
      for line in formatted_data:
        print(line)

      sleep(interval_sec)


if __name__ == '__main__':
  main(*argv[1:])  # pylint: disable=too-many-function-args
