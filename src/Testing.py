import json
import unittest
import networkx as nx
import time
from GraphAlgo import GraphAlgo
from networkx import *
import matplotlib.pyplot as plt
import calc


class Testing(unittest.TestCase):

    def test_Time_Short_Path_pyton(algo):
        path = '../data/G_10000_80000_1.json'
        algo = GraphAlgo()
        algo.load_from_json(path)


        start = time.time_ns()
        print(algo.shortest_path(4,34))
        end = time.time_ns()
        print("time1:",end-start)
        start = time.time_ns()
        print(algo.shortest_path(2,98))
        end = time.time_ns()
        print("time1:",end-start)

    def test_Time_connected_component_pyton(algo):
        path = '../data/G_10_80_0.json'
        algo = GraphAlgo()
        algo.load_from_json(path)

        start = time.time_ns()
        print(algo.connected_component(0))
        end = time.time_ns()
        print("time2:", end - start)
        start = time.time_ns()
        print(algo.connected_components())
        end = time.time_ns()
        print("time2:", end - start)

    def test_Time_Short_Path_networkx(algo):
        path = '../data/G_30000_240000_1.json'

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

        start = time.time_ns()
        print(nx.dijkstra_path(net_graph, 2, 98))
        end = time.time_ns()
        print("time3:", end - start)
        start = time.time_ns()
        print(nx.dijkstra_path(net_graph, 4, 34))
        end = time.time_ns()
        print("time3:", end - start)


    def test_Time_connected_component_etworkx(algo):
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


        start = time.time_ns()
        print(*nx.strongly_connected_components(net_graph))
        end = time.time_ns()
        print("time4:", end - start)





    # def test_networkx(self):
    #
    #     path = '../data/G_100_800_0.json'
    #
    #     nodes = []
    #     edges = []
    #
    #     with open(path) as f:
    #         data = json.load(f)
    #
    #        # print(data)
    #
    #         for n in data['Nodes']:
    #             nodes.append(n['id'])
    #
    #         for e in data['Edges']:
    #             edges.append((e['src'], e['dest'], e['w']))
    #
    #     net_graph = nx.DiGraph()
    #
    #     net_graph.add_nodes_from(nodes)
    #
    #     # (src, dest, w)
    #     net_graph.add_weighted_edges_from(edges)
    #
    #     algo = GraphAlgo()
    #     algo.load_from_json(path)
    #
    #     #print(algo.get_graph())
    #
    #     algo.plot_graph()

    # def test2(self):
    #     path = '../data/G_100_800_1.json'
    #
    #     nodes = []
    #     edges = []
    #
    #     with open(path) as f:
    #         data = json.load(f)
    #
    #         print(data)
    #
    #         for n in data['Nodes']:
    #             nodes.append(n['id'])
    #
    #         for e in data['Edges']:
    #             edges.append((e['src'], e['dest'], e['w']))
    #
    #     net_graph = nx.DiGraph()
    #
    #     net_graph.add_nodes_from(nodes)
    #
    #     # (src, dest, w)
    #     net_graph.add_weighted_edges_from(edges)
    #
    #     algo = GraphAlgo()
    #     algo.load_from_json(path)
    #
    #     start = time.time_ns()
    #     print(start)
    #     #print(algo.get_graph().get_all_v())
    #     #print(net_graph.nodes)
    #
    #
    #     #print(nx.shortest_path(net_graph, 4, 34))
    #     #print(algo.shortest_path(4,34))
    #     #print((nx.connected_components))
    #     #print(algo.connected_component(3))
    #     nx.draw_spring(net_graph,with_labels=True)
    #     plt.show()
    #     #nx.strongly_connected_components(net_graph)
    #     #nx.strongly_connected_components(net_graph)
    #     #nx.strongly_connected_components(net_graph)
    #     #nx.connected_components(net_graph)
    #     #algo.plot_graph()
    #
    #     #print(nx.shortest_path(net_graph,4,8))
    #     #nx.shortest_path(net_graph,200, 12049)
    #     #print(algo.shortest_path(200, 12049))
    #     #print(algo.connected_components())
    #     print(algo.connected_component(3))
    #     #print(algo.connected_component(3))
    #
    #     #algo.plot_graph()
    #
    #
    #     end = time.time_ns()
    #     print(end)
    #     print("time:", float(end-start))

if __name__ == '__main__':
    unittest.main()
