# Задание-2:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка

class Traffic_lights():

    def __init__(self, color_traffic_lights: str):

        self.color_traffic_light = color_traffic_lights



    def traffic(self):

        if self.color_traffic_light == ("red"):
            return "STOP"

        if self.color_traffic_light == ("green"):
            return "GO"

        if self.color_traffic_light == ("yellow"):
            return "WAIT"


traffic1 = Traffic_lights("red")

print(traffic1.traffic())