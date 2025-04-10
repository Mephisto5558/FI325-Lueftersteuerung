from datetime import datetime
import csv

def save_to_csv(
    file,
    temperature_c: float, temperature_f: float,
    humidity: int, air_pressure: int, dew_point_c: float, dew_point_f: float, timestamp: datetime
):
  """Write the data to the specified CSV"""
  data = dict(  # pylint:disable=use-dict-literal # better readability
      timestamp=timestamp,
      temperature_c=temperature_c,
      temperature_f=temperature_f,
      humidity=humidity,
      air_pressure=air_pressure,
      dew_point_c=dew_point_c,
      dew_point_f=dew_point_f
  )

  writer = csv.DictWriter(file, delimiter=';', fieldnames=(e for e in data))
  writer.writerow(data)
