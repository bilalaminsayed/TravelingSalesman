# Bilal Sayed C950 Greedy.py


# algorithm to heuristically calculate shorted path from starting node, touching all nodes, and back to start.
def alg(graph, initial):
    # creates copies from the graph
    nodes = graph.nodes
    edges = graph.edges
    distances = graph.distances

    # sets loop cursor to initial
    cursor = initial
    # dictionary to hold path with weights
    # adds initial to the lowest dictionary
    lowest = {cursor: 0}

    # removes initial from nodes set
    nodes.remove(initial)

    # removes the initial value from the adjacency lists
    for key in edges:
        if cursor in edges[key]:
            edges[key].remove(cursor)

    # start of main loop
    continue_loop = True
    while continue_loop:
        try:
            # reset temp dict
            temp = {}
            # for each adjacent vertex to the selected vertex
            for edge in edges[cursor]:
                # set the temp dict with each edge and weight adjacent to the selected vertex
                temp[edge] = distances[cursor, edge]

            # select the min distance in the temp dict and add to the lowed dict
            lowest[(min(temp, key=temp.get))] = (temp[min(temp, key=temp.get)])
            # set the cursor to the found vertex
            cursor = (min(temp, key=temp.get))

            # for key in edges
            for key in edges:
                # if the cursor is in the adjacency list
                if cursor in edges[key]:
                    # remove it so it cannot be visited again
                    edges[key].remove(cursor)
            # remove the cursor from the list of nodes
            nodes.remove(cursor)

        except ValueError:
            # stop loop
            continue_loop = False

        # add the weight from the last vertex back to the hub
        lowest[initial] = distances[cursor, initial]

    # sum of the total distance traveled
    sum_of_distances = sum(lowest.values())

    # return total distance and path
    return sum_of_distances, lowest
