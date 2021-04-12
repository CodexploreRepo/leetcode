class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.lots = {3: small, 2: medium, 1: big}

    def addCar(self, carType: int) -> bool:
        lot = self.lots[carType]
        if lot != 0:
            self.lots[carType]-= 1
            return True
        else:
            return False
