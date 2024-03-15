from tire.tire import TireSet

class OctoPrimeSet(TireSet):
    def __init__(self, tires):
        self.tires = tires


    def needs_service(self):

        wear = sum(self.tires)

        return wear >= 3
