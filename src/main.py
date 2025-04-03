from sys import argv
from time import sleep
from datetime import datetime

def get_data():
  """Reads the data from the device"""
  
  ...
  
def format_data(temperature: float, humidity: float, air_pressure: float, timestamp: datetime) -> list[str]:
  """
  Returns a list of formatted data.
  :temperature float Temperature in celsius * 1000
  """
  
  temperature*=0.001 # conversion
  
  return [
    f'========== {timestamp.isoformat()} =========='
    , f'Temperatur (Celsius): {temperature:.2f} °C'
    , f'Temperatur (Fahrenheit): {temperature * 1.8 + 32:.2f} F'
    , f'Luftfeuchte: {int(humidity)} % r.F.'
    , f'Luftdruck: {int(air_pressure)} hPa'
    , ''
  ]

def main(interval_sec=10):
  """Run infinite loop with an interval"""
  
  while True:
    data = get_data()
    formatted_data = format_data(*data)
    
    for line in formatted_data: print(line)
    sleep(interval_sec)
  
if __name__ == '__main__':
  main(*argv)