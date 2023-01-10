from paho.mqtt.client import Client
from random import randint


class SolarPanel:
    @staticmethod
    def initialize_shield(index: int, client: Client, value: int):
        client.publish(f"SolarPanel/{index}/shield", value)
    @staticmethod
    def simulate(index: int, client: Client, day: int, weather: int):

        temperature = 0
        production = 0
        light = 0
        if day == 1:
            # day section
            match weather:
                case 0:
                    temperature = randint(20, 30)
                    production = randint(90, 100)
                    light = 10
                case 1:
                    temperature = randint(15, 25)
                    production = randint(70, 90)
                    light = 7
                case 2:
                    temperature = randint(10, 15)
                    production = randint(50, 70)
                    light = 5
                case 3:
                    temperature = randint(0, 10)
                    production = randint(20, 50)
                    light = 3
        else:
            # night section
            temperature = randint(0, 10)
            production = 0
            light = 0

        client.publish(f"solarPanel/{index}/temperature", temperature)
        client.publish(f"solarPanel/{index}/production", production)
        client.publish(f"solarPanel/{index}/light", light)