ID:314972902 Rinat Grinberg Gabi Dadashov 



The task was divided into 3 main parts that deals in python language:

The first part was implementation of the directed graph that used for the second and thierd part:

The graph contains an implementation of 2 classes:
DiNode.
GraphAlgo
DiGraph

DiNode.:
We built a new class (DiNode) that contian simple methods and similar arguments as last task
In addition, we added 
2 lists for each node that contains the edges that in to this node and out from this node.
def __repr__(self):
in order to check the tests.
This method returns string with node's vlaue: edges out and edges in.
The complexity of the all methods was O(1)

DiGraph:
we defined 3 protected variables : 
    _MC
    _edge_count = 0
    _node_count = 0


def __init__(self, dict_nodes= {}):
 we created a dictionary that include node_id in the key and the values in the val.
complexity O(1)

def add_node(self, node_id: int, pos: tuple = None) -> bool:
 Allows to add a new node to the dictionary. the method checks if the node already exist, if yes,the method doesnt add the node. if the node not exist the method adds a new node to nodes dictionary. the _MC Increases by 1
Complexity O(1)

def add_edge(self, id1: int, id2: int, weight: float) -> bool:
 The method adds a new edge between 2 nodes(src, dest).
 the method checks several conditions,in order to connect the nodes: 
  if id1 in self.nodes and id2 in self.nodes:
	if id1 is not id2 and weight > 0:
 Existence of all conditions makes it possible to connect the new edge. the _MC and edge_count Increase by 1.
 Complexity O(1)

def get_all_v(self) -> dict:
Return the all nodes from the Graph. return the dictionary
Complexity O(1)

def all_in_edges_of_node(self, id1: int) -> dict:
Return the all edges that outs from the id1. dictionary that representing all the edges getting out of the given node (ID). 
Complexity O(1)

def remove_node(self, node_id: int) -> bool:
The method remove node by ID. the method checks if the node is already exists if not:
the method removes all the adges the ins to the node and outs from the node. 
After that the methods remove it.
edge_count decrease by 1 _MC Increase by 1
Complexity O(|V|)

def remove_edge(self, node_id1: int, node_id2: int) -> bool: 
The mothod disconnect edge between src and dest. The method checks several conditions,in order to disconnect the edge: 
 if node_id1 in self.nodes and node_id2 in self.nodes:
    if node_id2 in node1.outs and node_id1 in node2.ins:
               if node_id1 is not node_id2:
Existence of all conditions makes it possible to disconnect necessary edge.
note: it also remove relation between node.
edge_count decrease by 1 mode_count decreases by 1
Complexity O(1)


def e_size(self) -> int:
Return the edge_Size in the graph.
complexity O(1)

def get_mc(self) -> int:
Return the mode_count in the graph. 
complexity O(1)

 def v_size(self) -> int:
 Return the node_size in the graph. 
complexity O(1)

 def __eq__(self, other):
        return other.node_size == self.node_size and other.edge_size == self.edge_size
this methods check if two graphs are equal.
complexity O(1)

 def __repr__(self):
        return f"|V|={self.node_size} , |E|={self.edge_size}"
this methods returns string of the nodes and the edges in the graph.

===========================================================================================================
GraphAlgo:

we built a new class (GraphAlgo) that contian complexity methods.
The class contains: public DiGraph graph;  

 def __init__(self, g=None):
        self.graph = g

Initialize the graph with self.graph =g. 
Complexity O(1)

 def get_graph(self) -> GraphInterface:
return the directed graph on which the algorithm works on
Complexity O(1)

def djikstra(self, source: int) -> None:
the method calculate the shortest distance between src to dest. use PriorityQueue for save the lowest distance
For start, the method init the dostance for each node. and the prev for each node = None.
after that, using for loop in order to check all the node and calculate the distance.
complexity O(|E*V|)


def shortest_path_Number (self, id1: int, id2: int) -> float:
The method operates djikstra in order to return the lowest distance.
it returns a list with the distance to id2.
complexity O(|E*V|)

def shortest_path(self, id1: int, id2: int) -> (float, list):
The method operates shortest_path_Number(id1,id2) in order to return list of nodes of this Path. 
creating List of nodes and the result of the djikstra put on this list and reverse the nodes. 
complexity O(|E*V|)

def DFS(self):
In order to calculate if the graph is connected we used DFS. 
we declared boolean array: visited=[] This array served us to know if from any node it is possible to reach our neighbor.

def DFS_init(self, vertex, visited, true=None):
Initialize the array: visited[vertex]=true. 
using edgeNeighbor in order to check connected_component for each node.
the complexity of all DFS is O(|E*V|)

def connected_components(self) -> List[list]:
The method operates DFS() method, in DFS we calculated the connected_components.
After that the DFS returns the result.
complexity O(|E*V|)

def connected_component(self, id1: int) -> list:
using DFS and return list with the results.
the method returns the res[id1].
complexity O(|E*V|)

def load_from_json(self, file_name: str) -> bool:
this method try to read the gson file ti graph. 
using json.load(f), in order to recieve the data and order it properly we used For loop and over on all the nodes.
in the end we use  OSError if the loading was failled.
complexity O(|E*V|)


def save_to_json(self, file_name: str) -> bool:
save the result into file. the method Json.dump(data,f), FileWriter Passes about all the nodes and all the edges and insert them to 
the file . for end the process, if the saving was fall, triggerd IOException operates and return false.
complexity O(|E*V|)

def plot_graph(self) -> None:
import matplotlib.pyplot as plt
Because we have 2 types of files we divided the function to 2 cases in order to match the file's structure. 
We checked if the new file is contains a pos in order to find ditterences: 
if n.pos: -> the file contains already a position of X Y Z coordinates 
use X1 X2 Y1 Y2 in order to locate the points and doing arrorws. 
plt.arrow(x1, y1, dx_index * pro, dy_index * pro, head_width=0.0020, width=0.0001, color="black")
plt.scatter(x1, y1, s=25, color="red")

TESTS: creating test files and sampled end cases like inserting / lowering a side twice null And various exceptions.