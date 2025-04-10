from datetime import datetime
from sensor import format_data, calc_data  # Import der Funktion aus der anderen Datei

def test_data_darstellen():
  """Testet, ob format_data korrekte Ausgaben bei gültigen Sensorwerten liefert."""
  temperatur = 22000  # Celsius
  feuchtigkeit = 55  # Prozent
  luftdruck = 1013  # hPa
  timestamp = datetime(2025, 3, 27, 12, 8, 50)
  data = calc_data(temperatur, feuchtigkeit, luftdruck, timestamp)

  expected_data = [
    "========== 2025-03-27_ 12:08:50 ==========",
    "Temperatur (Celsius): 22.00 °C",
    "Temperatur (Fahrenheit): 71.60 F",
    "Luftfeuchte: 55 % r.F.",
    "Luftdruck: 10130 hPa",
    ""
  ]

  formatted_data = format_data(*data)

  print("Testfall 1: Sensordaten korrekt darstellen")
  for expected, actual in zip(expected_data, formatted_data):
    if expected == actual:
      print(f"Erfolgreich: {expected}")
    else:
      print(f"Fehler: Erwartet: {expected}, aber erhalten: {actual}")

def test_invalid_data_darstellen():
  """Testet, ob format_data bei ungültigen Werten keine Daten zurückgibt."""
  temperatur = None
  feuchtigkeit = None
  luftdruck = None
  timestamp = None

  expected_data = []
  formatted_data = format_data(temperatur, feuchtigkeit, luftdruck, timestamp)

  print("Testfall 2: Keine Daten bei ungültigen Werten")
  if formatted_data == expected_data:
    print("Erfolgreich: Keine Daten dargestellt (leere Liste)")
  else:
    print(f"Fehler: Erwartet: {expected_data}, aber erhalten: {formatted_data}")

def run_tests():
  """Führt alle Tests aus."""
  test_data_darstellen()
  print("-" * 50)
  test_invalid_data_darstellen()

if __name__ == "__main__":
  run_tests()
