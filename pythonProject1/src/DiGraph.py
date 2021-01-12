from DiNode import DiNode
import random


class DiGraph:

    def __init__(self, graph=None):
        self.nodes = {}

        self.mc = 0
        self.edge_size = 0
        self.node_size = 0
        self.pos0 = {}

    def __eq__(self, other):
        return other.node_size == self.node_size and other.edge_size == self.edge_size

    def __repr__(self):
        return f"|V|={self.node_size} , |E|={self.edge_size}"

    def v_size(self) -> int:

        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.node_size

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edge_size

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using apair  (key, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        try:
            node = self.nodes[id1]
            return node.ins
        except TypeError as e:
            return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        try:
            node = self.nodes[id1]
            return node.outs
        except TypeError as e:
            return None

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 in self.nodes and id2 in self.nodes:
            if id1 is not id2 and weight > 0:

                n1 = self.nodes[id1]
                n2 = self.nodes[id2]

                # if edge already exists!
                if id2 not in n1.outs and id1 not in n2.ins:
                    n1.outs[id2] = weight
                    n2.ins[id1] = weight

                    self.mc += 1
                    self.edge_size += 1

                    return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

        x1, y1, z1 = random.random() * 9, random.random() * 9, 0
        self.pos0[node_id] = [x1, y1]
        if node_id not in self.nodes:

            self.nodes[node_id] = DiNode(node_id, pos)

            self.node_size += 1
            self.mc += 1

            return True

        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """

        if node_id in self.nodes:

            remove_node = self.nodes[node_id]

            outs = remove_node.outs
            ins = remove_node.ins

            for key in outs:
                del self.nodes[key].ins[node_id]
                self.edge_size -= 1
                self.mc += 1

            for key in ins:
                del self.nodes[key].outs[node_id]

            del self.nodes[node_id]
            self.mc += 1
            self.node_size -= 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """

        if node_id1 in self.nodes and node_id2 in self.nodes:

            node1 = self.nodes[node_id1]
            node2 = self.nodes[node_id2]

            if node_id2 in node1.outs and node_id1 in node2.ins:

                if node_id1 is not node_id2:

                    del node1.outs[node_id2]
                    self.edge_size -= 1
                    del node2.ins[node_id1]
                    self.mc += 1

                    return True

        return False