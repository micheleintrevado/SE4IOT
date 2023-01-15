import time
import paho.mqtt.client as mqtt
from components.System import System
from components.hardware.SolarPanel import SolarPanel
from components.hardware.WindTurbine import WindTurbine

shield = [0, 0, 0, 0, 0]
running = [1, 1, 1]


def subscribe_solar(msg):
    index = int(msg.topic[-8])
    shield[index] = int(str(msg.payload.decode('utf-8')))


def subscribe_wind(msg):
    index = int(msg.topic[-9])
    running[index] = int(str(msg.payload.decode('utf-8')))


def main():
    system = System()
    client = mqtt.Client("ID1")
    client.on_publish = lambda client, userdata, mid: print("PUBLISH: ", mid)

    client_solar = mqtt.Client("ID3")
    client_solar.on_message = lambda client, userdata, msg: subscribe_solar(msg)

    client_wind = mqtt.Client("ID4")
    client_wind.on_message = lambda client, userdata, msg: subscribe_wind(msg)

    connected = False
    ip = "172.20.0.100"
    while not connected:
        try:
            if client.connect(ip) == 0 and client_solar.connect(ip) == 0 and client_wind.connect(ip) == 0:
                connected = True
        except:
            print("Connection failed")
            time.sleep(5)

    for index in range(0, 5):
        client_solar.subscribe(f"solarPanel/{index}/shield")

    for index in range(0, 3):
        client_wind.subscribe(f"windTurbine/{index}/running")

    for index in range(0, 5):
        SolarPanel.initialize_shield(index, client, 0)

    for index in range(0, 3):
        WindTurbine.initialize_running(index, client, 1)

    while True:

        system.publish(client)

        client_solar.loop_start()
        for index in range(0, 5):
            SolarPanel.simulate(index, client, system.day, system.weather, shield[index])
        client_solar.loop_stop()

        client_wind.loop_start()
        for index in range(0, 3):
            WindTurbine.simulate(index, client, system.wind, running[index])
        client_wind.loop_stop()

        time.sleep(30)


if __name__ == "__main__":
    main()
