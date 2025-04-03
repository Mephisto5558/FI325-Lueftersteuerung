import atexit
from sys import argv
from time import sleep

try: from RPi import GPIO # pylint:disable=import-error # not available on windows
except RuntimeError:
  print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.")

def get_data(channel):
  """Reads the data from the device"""

  return GPIO.input(channel)  # 0 = ON, 1 = OFF

def toggle_channel(channel):
  """Enables or disables the channel"""

  return GPIO.output(channel, not get_data(channel))

def setup_gpio():
  """Setup GPIO and register the exit handler."""

  @atexit.register
  def cleanup():
    print('Exiting script, cleaning up.')
    GPIO.output(channel, 1)  # turn off

    GPIO.cleanup()

  channel = 23  # 23 = Luefter

  print(f'[DEBUG]: {channel=}, {GPIO.RPI_INFO=}, {GPIO.VERSION=}')

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(channel, GPIO.IN)
  GPIO.setup(channel, GPIO.OUT)

  return channel

def main(interval_sec=10):
  """Run infinite loop with an interval"""

  channel = setup_gpio()

  while True:
    print(get_data(channel))
    sleep(interval_sec)

if __name__ == '__main__':
  main(*argv[1:]) # pylint: disable=too-many-function-args
