# Bilal Sayed C950 Package.py


# package class to hold package data with getters and setters
class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck_status = "N/A"
        self.truck_load_time = "Not on truck"
        self.status = "At Hub"
        self.delivery_time = "Undelivered"

    def __str__(self):
        return "PACKAGE ID: " + str(self.package_id) + ' | ADDRESS: ' + str(self.address) + ' ' + str(self.city) + ' ' + \
               str(self.state) + ' ' + str(self.zip) + ' | DEADLINE: ' + str(self.deadline) + ' | PACKAGE WEIGHT: ' + \
               str(self.weight) + ' | SPECIAL INSTRUCTIONS: ' + str(self.notes) + ' | LOADED ON: ' + \
               str(self.truck_status) + str(self.truck_load_time) + '| STATUS: ' + str(self.status) + ' ' + \
               str(self.delivery_time)

    __repr__ = __str__

    def get_package_id(self):
        return self.package_id

    def set_package_id(self, package_id):
        self.package_id = package_id

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_zip(self):
        return self.zip

    def set_zip(self, zip):
        self.zip = zip

    def get_deadline(self):
        return self.deadline

    def set_deadline(self, deadline):
        self.deadline = deadline

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def get_truck_status(self):
        return self.truck_status

    def set_truck_status(self, truck_status):
        self.truck_status = truck_status

    def get_truck_load_time(self):
        return self.truck_load_time

    def set_truck_load_time(self, truck_load_time):
        self.truck_load_time = truck_load_time

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_delivery_time(self):
        return self.delivery_time

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time
