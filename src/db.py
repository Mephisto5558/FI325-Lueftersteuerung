from datetime import datetime
import sqlite3 as sqlite

def connect(connection_sting):
  """Connect to the DB, returns connection and cursor."""

  connection = sqlite.connect(connection_sting)
  cursor = connection.cursor()

  return connection, cursor

def save(
  cursor: sqlite.Cursor,
  sensorID: int, statusID: int,
  temperature: float, humidity: float, air_pressure: float,
  timestamp: datetime
):
  """Saves data given to the DB"""

  result = cursor.execute(
    """
    INSERT INTO messung(sensorID, statusID, timestamp)
    VALUES(:1, :2, :3)
    """, (sensorID, statusID, timestamp.isoformat(timespec='seconds').replace('T', '_ '))
  )

  cursor.execute(
    """
    INSERT INTO Messwert(messungID, typID, wert)
    VALUES(:1, :2, :3)
    """, (messungID, typID, wert)
  )


def get():
  """Read data from DB"""
  ...
