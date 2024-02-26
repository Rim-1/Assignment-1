class Passenger:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

class Flight:
    def __init__(self, flight_name, flight_num,
                 departure, arrival, destination,date, electronic_ticket):
        self.flight_name = flight_name
        self.flight_num = flight_num
        self.departure = departure
        self.arrival = arrival
        self.destination = destination
        self.date = date
        self.et = electronic_ticket
    def displaydetails(self):
        print(f"Flight:{self.flight_name}\nNumber:{self.flight_num}\n"
              f"Departure: {self.departure}\nArrival: {self.arrival}\n"
              f"Date: {self.date}\nElectronic ticket: {self.et}")

class Seat:
    def __init__(self, seat_num, seat_class):
        self.seatn = seat_num
        self.seatcl = seat_class

    def displayseat(self):
        print(f"Seat: {self.seatn}\nClass: {self.seatcl}")

class BoardingPass:
    def __init__(self, passengerinfo, flightinfo,
                 seatinfo, gate, terminal):
        self.passengerinfo = passengerinfo
        self.flightinfo = flightinfo
        self.seatinfo = seatinfo
        self.gate = gate
        self.terminal = terminal

    def displayboardingpass(self):
        print("Boarding Pass:")
        print(f"Name: {self.passengerinfo.get_name()}")
        self.flightinfo.displaydetails()
        self.seatinfo.displayseat()
        print(f"Gate: {self.gate}, Terminal: {self.terminal}")

passenger1 = Passenger("James Smith")
flight1 = Flight("National Airlines", "NA4321","11:40",
                 "13:20", "From: CHICAGO ORD, TO:NEW YORK JFK",
                 "06 DEC 20", "629")
seat1 = Seat("09A", "First Class")
gate = ("03")
terminal = ("2")
boardingpass = BoardingPass(passenger1, flight1, seat1,
                            gate, terminal)
boardingpass.displayboardingpass()