from random import randint
from paho.mqtt.client import Client


class WindTurbine:
    @staticmethod
    def simulate(index: int, client: Client, wind: int):

        speed = 0
        production = 0
        vibration = 0

        match wind:
            case 0:
                speed = randint(0, 5)
                production = randint(10, 30)
                vibration = 2
            case 1:
                speed = randint(15, 25)
                production = randint(30, 70)
                vibration = 4
            case 2:
                speed = randint(30, 40)
                production = randint(70, 100)
                vibration = 8

        client.publish(f"windTurbine/{index}/speed", speed)
        client.publish(f"windTurbine/{index}/production", production)
        client.publish(f"windTurbine/{index}/vibration", vibration)