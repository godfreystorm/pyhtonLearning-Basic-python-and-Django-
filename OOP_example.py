class Flight():
    def __init__(self, capacity):
        self.capcity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capcity - len(self.passengers)
    
flight = Flight(3)


people = ["Godfrey", "Bill", "Joshua", "Alvin"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to the flight successfully!")
    else:
        print(f"No availabale seats for {person}")
