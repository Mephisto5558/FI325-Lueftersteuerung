# Test-Cases für die Speicherung von Sensordaten

### Case 1: Sensordaten speichern (Temperatur, Feuchtigkeit und Zeitstempel)

    Ziel: Überprüfen, ob die Sensordaten korrekt gespeichert werden, wenn Temperatur, Feuchtigkeit und Zeitstempel übergeben werden.

    Eingaben: Temperatur = 22°C, Feuchtigkeit = 55%, Zeitstempel = 2025-03-27 12:08:50

    Erwartetes Ergebnis: Daten werden mit korrekten Werten gespeichert.

### Case 2: Keine Sensordaten speichern, wenn ungültige Werte übergeben werden

    Ziel: Überprüfen, ob keine Daten gespeichert werden, wenn ungültige Werte übergeben werden.

    Eingaben: Temperatur = None, Feuchtigkeit = None, Zeitstempel = None

    Erwartetes Ergebnis: Keine Daten werden gespeichert.

<br>

# Test-Cases für die Lüfterregelung

### Case 3: Lüfter einschalten, wenn die Temperatur über dem Schwellenwert liegt

    Ziel: Überprüfen, ob der Lüfter eingeschaltet wird, wenn die Temperatur über dem definierten Schwellenwert liegt.

    Eingaben: Temperatur = 32°C, Schwellenwert = 30°C

    Erwartetes Ergebnis: Lüfterstatus = True

### Case 4: Lüfter ausschalten, wenn die Temperatur unter dem Schwellenwert liegt

    Ziel: Überprüfen, ob der Lüfter ausgeschaltet wird, wenn die Temperatur unter dem definierten Schwellenwert liegt.

    Eingaben: Temperatur = 28°C, Schwellenwert = 30°C

    Erwartetes Ergebnis: Lüfterstatus = False

<br>

# Test-Cases für Lüfterregelung und Sensordatenspeicherung zusammen

Case 5: Lüftersteuerung und Sensordaten speichern basierend auf der Temperatur

    Ziel: Überprüfen, ob die Sensordaten korrekt gespeichert und der Lüfter entsprechend der Temperaturregelung ein- oder ausgeschaltet wird.

    Eingaben: Temperatur = 32°C, Feuchtigkeit = 60%, Schwellenwert = 30°C, Zeitstempel = 2025-03-27 12:08:50

    Erwartetes Ergebnis: Lüfterstatus = True und die Daten werden korrekt gespeichert.

### Case 6: Lüftersteuerung und Sensordaten speichern bei Temperatur unter dem Schwellenwert

    Ziel: Überprüfen, ob die Sensordaten korrekt gespeichert und der Lüfter entsprechend der Temperaturregelung ausgeschaltet wird, wenn die Temperatur unter dem Schwellenwert liegt.

    Eingaben: Temperatur = 28°C, Feuchtigkeit = 50%, Schwellenwert = 30°C, Zeitstempel = 2025-03-27 12:08:50

    Erwartetes Ergebnis: Lüfterstatus = False und die Daten werden korrekt gespeichert.
