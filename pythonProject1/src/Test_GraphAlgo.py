from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from datetime import datetime
import unittest

def check0():

    g = DiGraph()  # creates an empty directed graph

    for n in range(8):
        g.add_node(n)

    g.add_node(25)
    print(f"test add existing node (false): {g.add_node(3)}")

    g.add_edge(0, 1, 1)

    print(f"test add existing edge (false): {g.add_edge(0, 1, 152)}")

    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(3, 1, 1.9)


    g.remove_edge(3, 1)

    print(f"remove non-existing edge (false): {g.remove_edge(1, 3)}")

    g.add_edge(3, 1, 10)

    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    algo_test = GraphAlgo(g)
    print(algo_test.shortest_path(0, 3))
    algo_test.plot_graph()
    print("connected component: ",algo_test.connected_component(0))


    algo_test.save_to_json("./data/test_load.json")

    algo_test1 = GraphAlgo()
    algo_test1.load_from_json("./data/test_load.json")

    g_algo = algo_test1.get_graph()
    print(g_algo)  # prints the __repr__ (func output)
    print(g_algo.get_all_v())  # prints a dict with all the graph's vertices.
    print(g_algo.all_in_edges_of_node(1))
    print(g_algo.all_out_edges_of_node(1))

    algo_test1.plot_graph()

    print("time: ", datetime.now())

    if g_algo == g:
        print("equals?")

    else:
        print("not equals")

    print("remove edge: (true): ", g_algo.remove_edge(1, 0))

    if g_algo == g:
        print("equals?")
    else:
        print("not equals")

    g1 = DiGraph()  # creates an empty directed graph

    for n in range(8):
        g1.add_node(n)

    g1.add_node(25)
    g1.add_edge(0, 1, 1)
    g1.add_edge(1, 0, 1.1)
    g1.add_edge(1, 2, 1.3)
    g1.add_edge(2, 3, 1.1)
    g1.add_edge(2, 3, 2)
    g1.add_edge(1, 3, 1.9)
    g1.add_edge(3, 5, 20)
    g1.add_edge(5, 6, 24)
    g1.add_edge(25, 6, 4)

    algo_test2 = GraphAlgo(g1)
    algo_test2.plot_graph()
    # algo_test2.connected_components()
    print(algo_test2.shortest_path(1, 6))
    print(algo_test2.shortest_path(2, 6))
    print(algo_test2.shortest_path(6, 1))
    print(algo_test2.shortest_path(3, 1))
    print(algo_test2.connected_component(1))





if __name__ == '__main__':
    check0()
