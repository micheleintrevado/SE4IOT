from paho.mqtt.client import Client
from random import randint
import requests


class SolarPanel:
    @staticmethod
    def initialize_shield(index: int, client: Client, value: int):
        client.publish(f"solarPanel/{index}/shield", value, retain=True)

    @staticmethod
    def simulate(index: int, client: Client, day: int, weather: int, shield: int):

        temperature = 0
        production = 0
        light = 0
        http_request = "http://172.20.0.105:5000/predictions/solar/"
        if day == 1:
            # day section
            match weather:
                case 0:
                    temperature = randint(20, 30)
                    # production = randint(90, 100)
                    light = 10
                case 1:
                    temperature = randint(15, 25)
                    # production = randint(70, 90)
                    light = 7
                case 2:
                    temperature = randint(10, 15)
                    # production = randint(50, 70)
                    light = 5
                case 3:
                    temperature = randint(0, 10)
                    # production = randint(20, 50)
                    light = 3
            http_request = http_request + str(light)
            production = requests.get(http_request)
            production = int(production.content)
        else:
            # night section
            temperature = randint(0, 10)
            production = 0
            light = 0

        if shield == 0:
            client.publish(f"solarPanel/{index}/temperature", temperature, retain=True)
            client.publish(f"solarPanel/{index}/production", production, retain=True)
            client.publish(f"solarPanel/{index}/light", light, retain=True)
        else:
            client.publish(f"solarPanel/{index}/temperature", 0, retain=True)
            client.publish(f"solarPanel/{index}/production", 0, retain=True)
            client.publish(f"solarPanel/{index}/light", 0, retain=True)
