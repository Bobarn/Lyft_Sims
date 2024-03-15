from tire.tire import TireSet

class CarriganSet(TireSet):
    def __init__(self, tires):
        self.tires = tires


    def needs_service(self):

        for tire in self.tires:

            if tire >= 0.9:
                return True

        return False
