# test_sensor.py

from datetime import datetime
from sensor import format_data  # Import der Funktion aus der anderen Datei

# Testfall 1: Sensordaten korrekt darstellen
def test_data_darstellen():
    temperatur = 22  # Temperatur in Celsius
    feuchtigkeit = 55  # Feuchtigkeit in Prozent
    luftdruck = 1013  # Luftdruck in hPa
    timestamp = datetime(2025, 3, 27, 12, 8, 50)  # Zeitstempel

    # Erwartete formatierte Daten
    expected_data = [
        "========== 2025-03-27_ 12:08:50 ==========",
        "Temperatur (Celsius): 22.00 °C",
        "Temperatur (Fahrenheit): 71.60 F",
        "Luftfeuchte: 55 % r.F.",
        "Luftdruck: 10130 hPa",
        ""
    ]

    # Tatsächliche formatierte Daten
    formatted_data = format_data(temperatur, feuchtigkeit, luftdruck, timestamp)

    # Überprüfen, ob die erwarteten und tatsächlichen Daten übereinstimmen
    print("Testfall 1: Sensordaten korrekt darstellen")
    for expected, actual in zip(expected_data, formatted_data):
        if expected == actual:
            print(f"Erfolgreich: {expected}")
        else:
            print(f"Fehler: Erwartet: {expected}, aber erhalten: {actual}")

# Testfall 2: Keine Daten darstellen, wenn ungültige Werte übergeben werden
def test_invalid_data_darstellen():
    # Ungültige Eingabewerte (None)
    temperatur = None
    feuchtigkeit = None
    luftdruck = None
    timestamp = None

    # Erwartetes Ergebnis: leere Liste, da ungültige Werte
    expected_data = []

    # Tatsächliche formatierte Daten
    formatted_data = format_data(temperatur, feuchtigkeit, luftdruck, timestamp)

    # Überprüfen, ob keine Daten zurückgegeben werden
    print("Testfall 2: Keine Daten bei ungültigen Werten")
    if formatted_data == expected_data:
        print("Erfolgreich: Keine Daten dargestellt (leere Liste)")
    else:
        print(f"Fehler: Erwartet: {expected_data}, aber erhalten: {formatted_data}")

# Hauptfunktion zum Ausführen der Tests
def run_tests():
    test_data_darstellen()  # Test 1: Sensordaten korrekt darstellen
    print("-" * 50)  # Trenner zwischen den Tests
    test_invalid_data_darstellen()  # Test 2: Keine Daten bei ungültigen Werten

# Tests ausführen
if __name__ == "__main__":
    run_tests()
