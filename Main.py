# Bilal Sayed C950 Main.py

from datetime import datetime
from Truck import Truck
import PackageData


# main function
def main():
    # create 3 truck objects
    truck_1 = Truck("Truck 1", 8, 0, 0, 'truck_1_vertices.csv', 'truck_1_edges.csv')
    truck_2 = Truck("Truck 2", 9, 0o5, 0, 'truck_2_vertices.csv', 'truck_2_edges.csv')
    truck_3 = Truck("Truck 3", 10, 20, 0, 'truck_3_vertices.csv', 'truck_3_edges.csv')

    # console ui
    total = truck_1.total + truck_2.total + truck_3.total
    print("******************************************")
    print("* Welcome to the WGUPS Delivery Tracker. *\n"
          "*                                        *\n"
          "* All packages delivered in ", total, "miles.*")
    print("******************************************")

    # user input
    loop = True
    while loop:
        try:
            print("1 to look up package id")
            print("2 to look up package id at a certain time")
            print("3 to get all packages")
            print("4 to get all packages at a certain time")
            user_input = int(input())
            if user_input == 1:
                user_input = int(input("Enter package id to track: "))
                print(PackageData.ht.get(user_input))
            if user_input == 2:
                user_input_package_id = int(input("Enter package id to track: "))
                user_input_time = str(input("Enter time (HH:MM) to track: "))
                time_conversion = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                           int(user_input_time[0:2]), int(user_input_time[3:5]), 0)
                if PackageData.ht.get(user_input_package_id).get_delivery_time() > time_conversion:
                    if PackageData.ht.get(user_input_package_id).get_truck_load_time() > time_conversion:
                        print("PACKAGE ID: " + str(
                            PackageData.ht.get(user_input_package_id).get_package_id()) + ' | ADDRESS: ' +
                              str(PackageData.ht.get(user_input_package_id).get_address()) + ' ' +
                              str(PackageData.ht.get(user_input_package_id).get_city()) + ' ' +
                              str(PackageData.ht.get(user_input_package_id).get_state()) + ' ' +
                              str(PackageData.ht.get(user_input_package_id).get_zip()) + ' | DEADLINE: ' +
                              str(PackageData.ht.get(user_input_package_id).get_deadline()) + ' | PACKAGE WEIGHT: ' +
                              str(PackageData.ht.get(
                                  user_input_package_id).get_weight()) + ' | SPECIAL INSTRUCTIONS: ' +
                              str(PackageData.ht.get(
                                  user_input_package_id).get_notes()) + ' | LOADED AT: At Hub' + ' | STATUS: Undelivered ')
                    else:
                        print("PACKAGE ID: " + str(
                            PackageData.ht.get(user_input_package_id).get_package_id()) + ' | ADDRESS: ' +
                              str(PackageData.ht.get(user_input_package_id).get_address()) + ' ' +
                              str(PackageData.ht.get(user_input_package_id).get_city()) + ' ' +
                              str(PackageData.ht.get(user_input_package_id).get_state()) + ' ' +
                              str(PackageData.ht.get(user_input_package_id).get_zip()) + ' | DEADLINE: ' +
                              str(PackageData.ht.get(user_input_package_id).get_deadline()) + ' | PACKAGE WEIGHT: ' +
                              str(PackageData.ht.get(
                                  user_input_package_id).get_weight()) + ' | SPECIAL INSTRUCTIONS: ' +
                              str(PackageData.ht.get(user_input_package_id).get_notes()) + ' | LOADED AT: ' +
                              str(PackageData.ht.get(user_input_package_id).get_truck_load_time()) +
                              str(PackageData.ht.get(
                                  user_input_package_id).get_truck_load_time()) + ' | STATUS: Undelivered ')
                else:
                    print("PACKAGE ID: " + str(
                        PackageData.ht.get(user_input_package_id).get_package_id()) + ' | ADDRESS: ' +
                          str(PackageData.ht.get(user_input_package_id).get_address()) + ' ' +
                          str(PackageData.ht.get(user_input_package_id).get_city()) + ' ' +
                          str(PackageData.ht.get(user_input_package_id).get_state()) + ' ' +
                          str(PackageData.ht.get(user_input_package_id).get_zip()) + ' | DEADLINE: ' +
                          str(PackageData.ht.get(user_input_package_id).get_deadline()) + ' | PACKAGE WEIGHT: ' +
                          str(PackageData.ht.get(user_input_package_id).get_weight()) + ' | SPECIAL INSTRUCTIONS: ' +
                          str(PackageData.ht.get(user_input_package_id).get_notes()) + ' | LOADED AT: ' +
                          str(PackageData.ht.get(user_input_package_id).get_truck_load_time()) +
                          str(PackageData.ht.get(user_input_package_id).get_truck_load_time()) + '| STATUS: ' +
                          str(PackageData.ht.get(user_input_package_id).get_status()) + ' ' +
                          str(PackageData.ht.get(user_input_package_id).get_delivery_time()))
            if user_input == 3:
                loop = 1
                for package in PackageData.ht:
                    print(PackageData.ht.get(loop))
                    loop += 1
            if user_input == 4:
                user_input_time = str(input("Enter time (HH:MM) to track: "))
                time_conversion = datetime(datetime.now().year, datetime.now().month, datetime.now().day,
                                           int(user_input_time[0:2]), int(user_input_time[3:5]), 0)
                loop = 1
                for package in PackageData.ht:
                    if PackageData.ht.get(loop).get_delivery_time() > time_conversion:
                        if PackageData.ht.get(loop).get_truck_load_time() > time_conversion:
                            print("PACKAGE ID: " + str(
                                PackageData.ht.get(loop).get_package_id()) + ' | ADDRESS: ' +
                                  str(PackageData.ht.get(loop).get_address()) + ' ' +
                                  str(PackageData.ht.get(loop).get_city()) + ' ' +
                                  str(PackageData.ht.get(loop).get_state()) + ' ' +
                                  str(PackageData.ht.get(loop).get_zip()) + ' | DEADLINE: ' +
                                  str(PackageData.ht.get(loop).get_deadline()) + ' | PACKAGE WEIGHT: ' +
                                  str(PackageData.ht.get(loop).get_weight()) + ' | SPECIAL INSTRUCTIONS: ' +
                                  str(PackageData.ht.get(
                                      loop).get_notes()) + ' | LOADED ON: At Hub' + ' | STATUS: Undelivered ')
                        else:
                            print("PACKAGE ID: " + str(
                                PackageData.ht.get(loop).get_package_id()) + ' | ADDRESS: ' +
                                  str(PackageData.ht.get(loop).get_address()) + ' ' +
                                  str(PackageData.ht.get(loop).get_city()) + ' ' +
                                  str(PackageData.ht.get(loop).get_state()) + ' ' +
                                  str(PackageData.ht.get(loop).get_zip()) + ' | DEADLINE: ' +
                                  str(PackageData.ht.get(loop).get_deadline()) + ' | PACKAGE WEIGHT: ' +
                                  str(PackageData.ht.get(loop).get_weight()) + ' | SPECIAL INSTRUCTIONS: ' +
                                  str(PackageData.ht.get(loop).get_notes()) + ' | LOADED ON: ' +
                                  str(PackageData.ht.get(loop).get_truck_status()) +
                                  str(PackageData.ht.get(loop).get_truck_load_time()) + ' | STATUS: Undelivered ')
                    else:
                        print("PACKAGE ID: " + str(
                            PackageData.ht.get(loop).get_package_id()) + ' | ADDRESS: ' +
                              str(PackageData.ht.get(loop).get_address()) + ' ' +
                              str(PackageData.ht.get(loop).get_city()) + ' ' +
                              str(PackageData.ht.get(loop).get_state()) + ' ' +
                              str(PackageData.ht.get(loop).get_zip()) + ' | DEADLINE: ' +
                              str(PackageData.ht.get(loop).get_deadline()) + ' | PACKAGE WEIGHT: ' +
                              str(PackageData.ht.get(loop).get_weight()) + ' | SPECIAL INSTRUCTIONS: ' +
                              str(PackageData.ht.get(loop).get_notes()) + ' | LOADED ON: ' +
                              str(PackageData.ht.get(loop).get_truck_status()) +
                              str(PackageData.ht.get(loop).get_truck_load_time()) + '| STATUS: ' +
                              str(PackageData.ht.get(loop).get_status()) + ' ' +
                              str(PackageData.ht.get(loop).get_delivery_time()))
                    loop += 1
        except:
            print("error")

        q = (str(input("continue? [Y/N]")))
        if q == "Y":
            continue
        else:
            loop = False


main()
