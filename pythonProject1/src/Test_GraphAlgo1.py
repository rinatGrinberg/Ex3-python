import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_something(self):
        g1 = DiGraph()  # creates an empty directed graph

        for n in range(8):
            g1.add_node(n)

        g1.add_node(25)
        g1.add_edge(0, 1, 1)
        g1.add_edge(1, 0, 1.1)
        g1.add_edge(1, 2, 1.3)
        g1.add_edge(2, 3, 1.1)
        g1.add_edge(1, 3, 1.9)
        g1.remove_edge(1, 3)
        g1.add_edge(1, 3, 10)

        # print(g1)  # prints the __repr__ (func output)
        # print(g1.get_all_v())  # prints a dict with all the graph's vertices.
        # (g1.all_in_edges_of_node(1))
        # print(g1.all_out_edges_of_node(1))

        algo_test = GraphAlgo(g1)
        algo_test.save_to_json('../data/G_10_80_0.json')

        algo_test1 = GraphAlgo()
        algo_test1.load_from_json('../data/G_10_80_0.json')

        g_algo = algo_test1.get_graph()
        # print(g_algo)  # prints the __repr__ (func output)
        # print(g_algo.get_all_v())  # prints a dict with all the graph's vertices.
        # print(g_algo.all_in_edges_of_node(1))
        # print(g_algo.all_out_edges_of_node(1))
        # algo_test1.plot_graph()

        self.assertEqual(g_algo, g1)
        self.assertEqual(g_algo.remove_edge(1, 0), True)
        # self.assertNotEqual(g_algo, g1)

        g1 = DiGraph()  # creates an empty directed graph

        for n in range(9):
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
        g1.add_edge(7, 25, 4)
        g1.add_edge(25, 7, 4)
        g1.add_edge(7, 8, 4)
        g1.add_edge(8, 25, 4)

        algo_test2 = GraphAlgo(g1)
        algo_test2.connected_component(25)
        algo_test2.plot_graph()
        #algo_test2.plot_graph()

        print(algo_test2.shortest_path(1, 6))
        print(algo_test2.shortest_path(2, 6))
        print(algo_test2.shortest_path(6, 1))
        print(algo_test2.shortest_path(3, 1))









if __name__ == '__main__':
    unittest.main()
