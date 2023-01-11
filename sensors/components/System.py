from paho.mqtt.client import Client
from random import randint

class System:
     weather : int
     wind : int
     day : int

     def publish(self, client : Client):
          self.weather = randint(0,3)
          self.wind = randint(0,2)
          self.day = randint(0,1)

          client.publish("system/weather", self.weather, retain=True)
          client.publish("system/wind", self.wind, retain=True)
          client.publish("system/day", self.day, retain=True)