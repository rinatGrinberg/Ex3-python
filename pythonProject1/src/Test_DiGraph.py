import unittest
from DiGraph import DiGraph
from src import GraphInterface


class MyTestCase(unittest.TestCase):

    def test_something(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(8):
            g.add_node(n)

        g.add_node(25)

        self.assertEqual(g.edge_size, 0)
        self.assertEqual(g.node_size, 9)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 2, 4)
        self.assertEqual(g.edge_size, 1)
        g.add_edge(2, 1, 4)
        g.add_edge(2, 7, 7)
        g.add_edge(0, 1, 12)
        n1 = g.nodes[1]
        self.assertEqual(n1.outs[2], 4)
        n2 = g.nodes[2]
        self.assertEqual(n2.outs[7], 7)
        allNodes = g.get_all_v()
        print(allNodes)
        self.assertEqual(g.add_edge(0, 1, 152), False)
        g.remove_node(5)
        self.assertEqual(g.remove_node(5), False)
        self.assertEqual(g.add_edge(5, 1, 6), False)
        self.assertEqual(g.node_size, 8)
        self.assertEqual(g.mc, 14)
        self.assertEqual(g.remove_edge(4, 3), False)
        print(g.all_in_edges_of_node(1))
        self.assertEqual(g.all_out_edges_of_node(1), {2: 4})
        self.assertEqual(g.all_out_edges_of_node(3), {})
        g.add_node(22)
        g.add_node(7)
        g.add_node(32)
        g.add_node(90)
        g.remove_node(22)
        g.remove_node(8)
        self.assertEqual(g.node_size, 10)
        self.assertEqual(g.mc, 18)
        self.assertEqual(g.all_out_edges_of_node(90), {})
        with self.assertRaises(Exception):
            g.all_out_edges_of_node(91)

        with self.assertRaises(Exception):
            g.all_in_edges_of_node(91)




if __name__ == '__main__':
    unittest.main()
