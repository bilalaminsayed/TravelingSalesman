# Bilal Sayed C950 Truck.py

from Graph import Graph
from Greedy import alg
from datetime import datetime
from datetime import timedelta
import PackageData
import csv


# truck class to hold trucks and calculate
class Truck:

    # define truck start time, and vertex and edge files
    def __init__(self, truck, h, m, s, vertex_file, edge_file):
        self.graph = Graph()
        self.departure_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, h, m, s)

        # read vertex file and add to graph
        with open(vertex_file, encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self.graph.add_node(int(row[0]))

        # read edge file and weights and add to graph
        with open(edge_file, encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self.graph.add_edge(int(row[0]), int(row[1]), float(row[2]))

        # run path finding algorithm on packages stored in graph
        self.total, self.path = alg(self.graph, 0)

        # calculate and assign package delivery time
        temp_path = self.path.copy()
        temp_path.pop(0)
        delivery_time = self.departure_time
        for package in temp_path:
            delivery_time += timedelta(hours=(temp_path.get(package) / 18))
            truck_status = str(truck) + " at: "
            PackageData.ht.get(package).set_truck_status(truck_status)
            PackageData.ht.get(package).set_truck_load_time(self.departure_time)
            PackageData.ht.get(package).set_status("Delivered at:")
            PackageData.ht.get(package).set_delivery_time(delivery_time)

        # calculate and assign truck return time
        self.return_time = (delivery_time + timedelta(hours=(self.path[0] / 18)))
