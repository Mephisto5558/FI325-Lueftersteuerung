from datetime import datetime
import csv

def save_to_csv(
    file,
    temperature_c: float, temperature_f: float,
    humidity: int, air_pressure: int, dew_point_c: float, dew_point_f: float, timestamp: datetime
):
  """Write the data to the specified CSV"""

  data = dict(  # pylint:disable=use-dict-literal # better readability
      timestamp=timestamp.isoformat(timespec='seconds').replace('T', ' '),
      temperature_c=temperature_c,
      temperature_f=temperature_f,
      humidity=humidity,
      air_pressure=air_pressure,
      dew_point_c=dew_point_c,
      dew_point_f=dew_point_f
  )

  writer = csv.DictWriter(file, delimiter=';', fieldnames=list(data))

  if file.tell() == 0: writer.writeheader() # write header only if file is empty
  writer.writerow(data)
