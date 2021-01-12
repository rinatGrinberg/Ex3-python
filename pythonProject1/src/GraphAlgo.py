import collections
from typing import List
from DiGraph import DiGraph
from src import GraphInterface
import json
import math
import heapq
import queue
import random

import sys
import matplotlib.pyplot as plt


class GraphAlgo:

    def __init__(self, g=None):
        self.graph = g
        self.prev = {}
        self.dist = {}
        self.menualPosition = {}

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        load_graph = DiGraph()

        try:
            # open file with 'r' - read option
            with open(file_name, 'r') as f:
                info = json.load(f)
                f.close()

            #print("loaded json: ", info)

            for n in info['Nodes']:

                try:

                    pos_string = n['pos'].split(",")
                    x, y, z = float(pos_string[0]), float(pos_string[1]), float(pos_string[2])

                    load_graph.add_node(n['id'], (x, y, z))

                except:
                    load_graph.add_node(n['id'])

            for e in info['Edges']:
                load_graph.add_edge(e['src'], e['dest'], e['w'])

            self.graph = load_graph
            return True

        except OSError as error:
            print("OSError: {}".format(error))
            return False
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """

        try:

            data = {}

            nodes = self.graph.get_all_v()

            data['Edges'] = []
            data['Nodes'] = []

            for n in nodes:
                node = nodes[n]

                if node.pos:
                    data['Nodes'].append({
                        "id": node.id,
                        "pos": node.pos
                    })
                else:
                    data['Nodes'].append({
                        "id": node.id
                    })

                for o in node.outs:
                    data['Edges'].append({
                        "src": node.id,
                        "dest": o,
                        "w": node.outs[o]
                    })

            f = open(file_name, 'w')
            json.dump(data, f)
            return True

        except OSError as e:
            print(f"OSError : {e}")
            return False

        except:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        length_Maslol = self.shortest_path_Number(id1, id2)
        runner = id2
        res = []
        if length_Maslol == float('inf'):
            print("not Maslol")
            return (-1, res)
        res.append(self.graph.nodes.get(id2))
        while True:
            if runner is id1: break
            res.append(self.graph.nodes.get(self.prev.get(runner)))
            runner = self.prev.get(runner)
        back_res = []
        for i in range(len(res) - 1, 0, -1):
            back_res.append(res.pop(i))

        back_res.append(self.graph.nodes.get(id2))
        return (length_Maslol, back_res)

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        visited, queue = set(), collections.deque([id1])
        visited.add(id1)
        res = []
        res.append(id1)
        while queue:

            # Dequeue a vertex from queue
            vertex = queue.popleft()
            nei = self.graph.nodes[vertex]
            res.append(vertex)

            # If not visited, mark it as visited, and
            # enqueue it

            t = self.graph.nodes[vertex]
            for neighbour in t.outs:
                nei= self.graph.nodes[neighbour]
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    res.append(neighbour)

        res.sort()
        mylist = list(dict.fromkeys(res))
        print(mylist)
        for i in mylist:
            nei = self.graph.nodes[i]
            if id1 not in nei.outs:
                print(i)
                #del mylist[i]


        return mylist


    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """

        connected = []

        # visit = {}
        # for k in self.graph.get_all_v():
        #     visit[k] = False
        nodes = self.graph.get_all_v()
        visit = {k: False for k in nodes}

        for key in nodes:
            if not visit[key]:
                self.DFS_init(key, visit, connected)

        # TRANSPOSE
        t_graph = DiGraph()
        for key in self.graph.get_all_v():
            t_graph.add_node(key)

        for key in self.graph.get_all_v():
            outs = self.graph.all_out_edges_of_node(key)
            for ni in outs:
                t_graph.add_edge(ni, key, outs[ni])

        visit = {k: False for k in nodes}
        list_of_components = []

        while connected:
            key = connected.pop()
            if not visit[key]:
                component = self.DFS(key, visit, [], t_graph)
                list_of_components.append(component)

        return list_of_components

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

        nodes = self.graph.nodes

        x_ = []
        y_ = []
        z_ = []

        for n in nodes:
            n = nodes[n]

            x, y, z = n.pos

            for e in n.outs:
                x1 = n.pos[0]
                y1 = n.pos[1]

                x2 = nodes[e].pos[0]
                y2 = nodes[e].pos[1]
                dx_index = (x2 - x1)
                dy_index = (y2 - y1)

                d_arrow = math.sqrt(dx_index ** 2 + dy_index ** 2)
                d_arrow_ex = math.sqrt(dx_index ** 2 + dy_index ** 2) + 0.00030 + 0.0001+0.0003
                pro = d_arrow / d_arrow_ex
                plt.arrow(x1, y1, dx_index * pro, dy_index * pro, head_width=0.0003, width= 0.00002, color="black")
                plt.scatter(x1, y1, s=30, color="red")
                plt.text(x1, y1 + 0.0001, str(n.id), color="green", fontsize=8)


        plt.ylabel('Gabi And Rinat Ex3')
        plt.xlabel('Gabi And Rinat Ex3')
        plt.show()

    def djikstra(self, source: int) -> None:
        queue.PriorityQueue()
        nodes = self.graph.get_all_v()
        q = queue.PriorityQueue()

        priority_queue = []

        for n in nodes:
            node = nodes[n]
            if node.id is source:
                self.dist.update({node.id: 0})
                self.prev.update({node.id: node.id})
                node.tag = 0

                priority_queue.append((0, node.id))
            else:
                self.dist.update({node.id: float('inf')})
                self.prev.update({node.id: None})
                node.tag = float('inf')

            # q.put_nowait(n)

        # prio_q is not NONE
        while priority_queue:
            # node1 = q.get()

            pr, node1 = heapq.heappop(priority_queue)

            for n in self.graph.nodes.get(node1).outs:

                nodefromgraph = self.graph.nodes.get(node1)
                neighborfromgraph = self.graph.nodes.get(n)

                alt = self.dist.get(nodefromgraph.id) + nodefromgraph.outs.get(neighborfromgraph.id)

                if alt < self.dist.get(neighborfromgraph.id):
                    self.dist.update({neighborfromgraph.id: alt})
                    self.prev.update({neighborfromgraph.id: nodefromgraph.id})

                    # q.get(neighborfromgraph.id)
                    # q.put_nowait(neighborfromgraph.id)

                    # in java we required decrease_priority
                    # to do it we did:
                    # remove + add
                    heapq.heappush(priority_queue, (alt, n))

    def shortest_path_Number(self, id1: int, id2: int) -> float:
        self.djikstra(id1)
        return self.dist.get(id2);

    def DFS_init(self, vertex, visited, connected):

        visited[vertex] = True

        for o in self.graph.all_out_edges_of_node(vertex):
            if not visited[o]:
                self.DFS_init(o, visited, connected)

        connected.append(vertex)



    def DFS(self, vertex, visited, components, transposed_graph):

        visited[vertex] = True

        components.append(vertex)

        for o in transposed_graph.all_out_edges_of_node(vertex):
            if not visited[o]:
                self.DFS(o, visited, components, transposed_graph)

        return components

