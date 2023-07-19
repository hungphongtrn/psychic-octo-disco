from class_oop import *

tool = ManagementTool()

# Add guests to the tool
guest1 = Person("Nguyen Van A", 25, "123456")
guest2 = VIP("Nguyen Van B", 30, "789012")
tool.add_guest(guest1)
tool.add_guest(guest2)

# Create room types
single_type = Type("Single", 100)
double_type = Type("Double", 150)
suite_type = Type("Suite", 200)

# Create rooms
room1 = Room("101", single_type)
room2 = Room("102", double_type)
room3 = Room("201", single_type)

# Add rooms to the tool
tool.rooms.extend([room1, room2, room3])

# Assign rooms to guests
guest1.room = room1
guest2.room = room2

# Set check-in and check-out dates for guests
checkin_date_guest1 = datetime(2023, 7, 1)
checkout_date_guest1 = datetime(2023, 7, 6)
guest1.checkin_date = checkin_date_guest1
guest1.checkout_date = checkout_date_guest1

checkin_date_guest2 = datetime(2023, 7, 2)
checkout_date_guest2 = datetime(2023, 7, 8)
guest2.checkin_date = checkin_date_guest2
guest2.checkout_date = checkout_date_guest2

# Calculate rental cost for a guest
rental_days = (checkout_date_guest1 - checkin_date_guest1).days
rental_cost = tool.calculate_rental_cost("123456", rental_days)
print(f"Rental cost for guest1: {rental_cost}")

# Show available and occupied rooms
tool.show_available_rooms()
tool.show_occupied_rooms()

# Calculate revenue
start_date = datetime(2023, 7, 1)
end_date = datetime(2023, 7, 10)
revenue = tool.calculate_revenue(start_date, end_date)
print(f"Revenue from {start_date} to {end_date}: {revenue}")
