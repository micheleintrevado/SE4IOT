from paho.mqtt.client import Client
from random import randint


class System:
    weather: int
    wind: int
    day: int
    light: int

    def publish(self, client: Client):
        self.weather = randint(0, 3)
        self.wind = randint(0, 2)
        self.day = randint(0, 1)

        if self.day == 1:
            match self.weather:
                case 0:
                    self.light = 10
                case 1:
                    self.light = 7
                case 2:
                    self.light = 5
                case 3:
                    self.light = 3
        else:
            self.light = 0

        client.publish("system/weather", self.weather, retain=True)
        client.publish("system/wind", self.wind, retain=True)
        client.publish("system/day", self.day, retain=True)
        client.publish("system/light", self.light, retain=True)
