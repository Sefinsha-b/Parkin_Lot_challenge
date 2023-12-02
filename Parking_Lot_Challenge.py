import random
import json

class ParkingLot:
    def __init__(self, square_footage, spot_size=(8,12)): 
        self.spot_size = spot_size
        self.parking_lot_size = square_footage // (spot_size[0] * spot_size[1])
        self.parking_lot = [None] * self.parking_lot_size
        self.parked_cars = {}

    def park_Car(self, car, spot):
        if self.parking_lot[spot] is None:
            self.parking_lot[spot] = car
            self.parked_cars[car.license_plate] = spot
            return True
        else:
            return False
    def map_to_json(self):
        return json.dumps(self.parked_cars, indent=2)
    
class Car:
    def __init__(self, license_plate): 
        self.license_plate = license_plate

    def __str__(self):
        return f"car with license plate {self.license_plate}"
    def park(self, parking_lot):
        spot = random.randint(0, len(parking_lot.parking_lot) -1)
        while not parking_lot.park_Car(self, spot):
            spot = random.randint(0, len(parking_lot.parking_lot) -1)
        print(f"{self} parked successfully in spot {spot}")

def main():
    parking_lot_size = 2000
    car_count = 20
    spot_size = (8,12)

    parking_lot = ParkingLot(parking_lot_size,spot_size)
    cars = [Car(f"{random.randint(1000000, 9999999)}") for _ in range(car_count)]
    while cars:
        car = cars.pop()
        car.park(parking_lot)

    print("parking lot is full")
    print("Mapping vehicles to spots:")
    print(parking_lot.map_to_json())

if __name__ == "__main__":
    main()


        