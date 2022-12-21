from random import randint
from paho.mqtt.client import Client

class FirstWindTurbine:
     @staticmethod
     def publish(client : Client, wind: int):

          match wind :
               case 0:
                    speed = randint(0,5)
                    production = randint(10,30)
                    vibration = 2
               case 1:
                    speed = randint(15,25)
                    production = randint(30,70)
                    vibration = 4
               case 2:
                    speed = randint(30,40)
                    production = randint(70,100)
                    vibration = 8
          
          client.publish("windTurbine1/speed", speed)
          client.publish("windTurbine1/production", production)
          client.publish("windTurbine1/vibration", vibration)