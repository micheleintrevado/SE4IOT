import time
from System import System
from Sensor1 import FirstSolarPanel
from Sensor2 import SecondSolarPanel
from WindTurbine1 import FirstWindTurbine
import paho.mqtt.client as mqtt

def main():
     system = System()
     client = mqtt.Client("ID1")
     client.on_publish = lambda client, userdata, mid: print("PUBLISH: ", mid)
     client.connect("localhost")
     while True:
          system.publish(client)
          FirstSolarPanel.publish(client, system.day, system.weather)
          SecondSolarPanel.publish(client, system.day, system.weather)
          FirstWindTurbine.publish(client, system.wind)

          time.sleep(10)

if __name__ == "__main__":
    main()
