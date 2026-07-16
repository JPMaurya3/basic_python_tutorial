class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car is starting")
class Toyato(Car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name =name
        super().start()
car1 = Toyato("prics","electric")
print(car1.type)