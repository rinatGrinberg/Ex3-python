import json
import unittest
import networkx as nx
import time
from GraphAlgo import GraphAlgo
from networkx import *
import matplotlib.pyplot as plt
import calc


class MyTestCase(unittest.TestCase):



    def test_connected_components_and_load(self):

     path = '../data/G_1000_8000_1.json'

     nodes = []
     edges = []

     with open(path) as f:
         data = json.load(f)

         # print(data)

         for n in data['Nodes']:
             nodes.append(n['id'])

         for e in data['Edges']:
             edges.append((e['src'], e['dest'], e['w']))

     net_graph = nx.DiGraph()

     net_graph.add_nodes_from(nodes)
     net_graph.add_weighted_edges_from(edges)

     algo = GraphAlgo()
     algo.load_from_json(path)

     print(*nx.strongly_connected_components(net_graph))
     b=algo.connected_component(416)
     self.assertEqual(b, [416])

    def test_Shortestpath_and_load(self):
        path = '../data/G_20000_160000_1.json'

        nodes = []
        edges = []

        with open(path) as f:
            data = json.load(f)

            # print(data)

            for n in data['Nodes']:
                nodes.append(n['id'])

            for e in data['Edges']:
                edges.append((e['src'], e['dest'], e['w']))

        net_graph = nx.DiGraph()

        net_graph.add_nodes_from(nodes)
        net_graph.add_weighted_edges_from(edges)

        algo = GraphAlgo()
        algo.load_from_json(path)

        SortPath_gabi_rinat_algo=algo.shortest_path(2,98)
        SortPath_networkx=nx.dijkstra_path(net_graph, 2, 98)
        a,b=SortPath_gabi_rinat_algo
        for i in range(len(b)):
            self.assertEqual(SortPath_networkx[i],b[i].id)

    def test_Plotgraph(self):
        path = '../data/A5'
        algo = GraphAlgo()
        algo.load_from_json(path)
        b=algo.plot_graph()
        self.assertEqual(b,None)








if __name__ == '__main__':
    unittest.main()
