import unittest
from DiGraph import DiGraph
from src import GraphInterface
import calc


class MyTestCase(unittest.TestCase):

    def test_nodesize_and_addnnode_and_removenode(self):
        g = DiGraph()
        for i in range(3):
            g.add_node(i)
        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(1)
        self.assertEqual(g.node_size,1)

    def test_edgesize_and_connect_and_remove_edge(self):
        g = DiGraph()
        for i in range(3):
            g.add_node(i)
        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(1)
        g.add_node(25)
        g.add_node(27)
        g.add_edge(25,2,1)
        g.add_edge(27,2,78)
        g.add_edge(2,25,3)
        g.add_node(7)
        g.add_node(8)
        g.add_node(9)
        g.add_edge(7,25,6)
        g.add_edge(8,25,16)
        g.add_edge(8,7,3)
        g.add_edge(9,2,11)
        g.add_edge(9,8,111)
        g.remove_edge(9,8)
        print(g.edge_size)
        self.assertEqual(g.edge_size,7)

    def test_get_v(self):
        g = DiGraph()
        for i in range(3):
            g.add_node(i)
        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(1)
        g.add_node(25)
        g.add_node(27)
        g.add_edge(25, 2, 1)
        g.add_edge(27, 2, 78)
        g.add_edge(2, 25, 3)
        g.add_node(7)
        g.add_node(8)
        g.add_node(9)
        g.add_edge(7, 25, 6)
        g.add_edge(8, 25, 16)
        g.add_edge(8, 7, 3)
        g.add_edge(9, 2, 11)
        g.add_edge(9, 8, 111)
        g.remove_edge(9, 8)
        nodes=g.get_all_v()
        self.assertIn(25,nodes)
        self.assertIn(7,nodes)
        self.assertIn(8,nodes)
        self.assertIn(9,nodes)
        self.assertIn(27,nodes)
        self.assertNotIn(1,nodes)

    def test_get_nodes_in_and_outs(self):
        g = DiGraph()
        for i in range(3):
            g.add_node(i)
        g.remove_node(0)
        g.remove_node(1)
        g.remove_node(1)
        g.add_node(25)
        g.add_node(27)
        g.add_edge(25, 2, 1)
        g.add_edge(27, 2, 78)
        g.add_edge(2, 25, 3)
        g.add_node(7)
        g.add_node(8)
        g.add_node(9)
        g.add_edge(7, 25, 6)
        g.add_edge(8, 25, 16)
        g.add_edge(8, 7, 3)
        g.add_edge(9, 2, 11)
        g.add_edge(9, 8, 111)
        g.remove_edge(9, 8)
        out = g.all_out_edges_of_node(2)
        inn = g.all_in_edges_of_node(2)
        self.assertIn(25, out)
        self.assertIn(27, inn)
        self.assertIn(25, inn)
        self.assertIn(9, inn)


if __name__ == '__main__':
    unittest.main()
