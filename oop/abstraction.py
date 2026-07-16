#abstraction is the process of hiding the internal details of an object and showing only the
#  essential features of the object.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"The engine of the {self.make} {self.model} is starting.")

        #python prints exactly what is written in the print statement. 
        # It does not add any extra information or formatting to the output.   
        # we use f-strings to format the output in a more readable way.


car1 = Car("Toyota", "Camry")
car1.start_engine()


class Car:
    def start_function(self,model,function):
        self.model = model
        self.function = function
        print("Engine started")
        print(f"The engine of the {self.model} is starting.")
        print(f"The engine of the {self.model} is stopping.")

# Main program
car = Car()
car.start_function("Toyota Camry", "start")  # This will raise an AttributeError since self.model is not defined in the Car class.
car.start_function("Honda city", "stop") 
