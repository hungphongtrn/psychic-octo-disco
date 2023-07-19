from datetime import datetime, timedelta

from datetime import datetime, timedelta


class Person:
    def __init__(self, full_name, age, id_number):
        self.full_name = full_name
        self.age = age
        self.id_number = id_number
        self.checkin_date = None
        self.checkout_date = None
        self.room = None


class VIP(Person):
    def __init__(self, full_name, age, id_number):
        super().__init__(full_name, age, id_number)

class Type:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Room:
    def __init__(self, name, room_type):
        self.name = name
        self.room_type = room_type
        self.guest = None


class ManagementTool:
    def __init__(self):
        self.room_types = []
        self.rooms = []
        self.guests = []

    def add_room_type(self, room_type):
        self.room_types.append(room_type)

    def remove_room_type(self, room_type):
        self.room_types.remove(room_type)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, id_number):
        for guest in self.guests:
            if guest.id_number == id_number:
                self.guests.remove(guest)
                break

    def calculate_rental_cost(self, id_number, rental_days):
        for guest in self.guests:
            if guest.id_number == id_number and guest.room is not None:
                room_type = guest.room.room_type
                price = room_type.price
                if isinstance(guest, VIP):
                    price *= 0.9  # 10% discount for VIP
                return rental_days * price
        return None

    def show_available_rooms(self):
        available_rooms = [room for room in self.rooms if room.guest is None]
        for room in available_rooms:
            print(f"Room: {room.name}, Type: {room.room_type.name}")

    def show_occupied_rooms(self):
        occupied_rooms = [room for room in self.rooms if room.guest is not None]
        for room in occupied_rooms:
            print(f"Room: {room.name}, Guest: {room.guest.full_name}")

    def calculate_revenue(self, start_date, end_date):
        revenue = 0
        for guest in self.guests:
            if guest.room and start_date <= guest.checkout_date <= end_date:
                rental_days = (guest.checkout_date - guest.checkin_date).days
                rental_cost = self.calculate_rental_cost(guest.id_number, rental_days)
                if rental_cost is not None:
                    revenue += rental_cost
        return revenue
