class Car:
    @staticmethod
    def start():
        print("car is starting")
    @staticmethod
    def stop():
        print("car is stopping")
class Toyato(Car):
    def __init__(self,model):
        self.model = model

car1 = Car()
car1.start()

class Tata(Toyato):
    def __init__(self, model):
        self.model = model
tata1 = Tata("haa")
print(tata1.model)