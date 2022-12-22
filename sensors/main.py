import time
import paho.mqtt.client as mqtt
from components.System import System
from components.hardware.SolarPanel import SolarPanel
from components.hardware.WindTurbine import WindTurbine


def main():
    system = System()
    client = mqtt.Client("ID1")
    client.on_publish = lambda client, userdata, mid: print("PUBLISH: ", mid)
    client.connect("localhost")
    while True:
        system.publish(client)

        for index in range(0, 2):
            SolarPanel.simulate(index, client, system.day, system.weather)

        for index in range(0, 1):
            WindTurbine.simulate(index, client, system.wind)

        time.sleep(10)


if __name__ == "__main__":
    main()
