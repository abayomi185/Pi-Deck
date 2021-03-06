import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

def gpio_cleanup():
  GPIO.cleanup()

class Pin:
  
  def __init__(self, pin_number):
      self.pin = pin_number
      self.is_virtual = False
      self.is_active = False

class Buttons():

  def __init__(self, user_pins):    
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering

    # self.pins2 = []
    # for x in range(len(user_pins)):
    #   self.pins2.append(Pin(user_pins[x]))

    self.pins = {}

    for x in range(len(user_pins)):
      #Assign pins into dictionary of Pin Classes using setdefault
      self.pins.setdefault(user_pins[x], Pin(user_pins[x]))

    self.init_pins()

  def init_pins(self):
    for key in self.pins:
      GPIO.setup(key, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
      # GPIO.add_event_detect(self.pins[x], GPIO.RISING, callback=send_input_to_client, 
      #                             bouncetime=200)

  def set_pin_callback(self, callback_func):
    for key in self.pins:
      GPIO.add_event_detect(key, GPIO.RISING, callback=callback_func, 
                                  bouncetime=200)

  def retrieve_values(self, channel):
    return (self.pins[channel].pin, self.pins[channel].is_virtual, self.pins[channel].is_active)


def main():
  pins = [26, 16, 12, 25, 24, 23]
  b = Buttons(pins)
  input("Press enter to exit ;)")

if __name__ == "__main__":
  main()