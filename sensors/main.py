import time
import paho.mqtt.client as mqtt
from components.System import System
from components.hardware.SolarPanel import SolarPanel
from components.hardware.WindTurbine import WindTurbine


def main():
    system = System()
    client = mqtt.Client("ID1")
    client.on_publish = lambda client, userdata, mid: print("PUBLISH: ", mid)
    connected = False
    while not connected:
        try:
            if client.connect("172.20.0.100") == 0:
                connected = True
        except:
            print("Connection failed")
            time.sleep(5)

    for index in range(0, 5):
        SolarPanel.initialize_shield(index, client, 0)

    for index in range(0, 3):
        WindTurbine.initialize_running(index, client, 1)

    while True:
        system.publish(client)

        for index in range(0, 5):
            SolarPanel.simulate(index, client, system.day, system.weather)

        for index in range(0, 3):
            WindTurbine.simulate(index, client, system.wind)

        time.sleep(30)


if __name__ == "__main__":
    main()
