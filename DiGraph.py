import math
from GraphInterface import GraphInterface


class NodeData:

    def __init__(self, key: int = None, tag: int = -1, weight=math.inf, visited: bool = False, info=None,
                 pos: tuple = None, edges_out=None, edges_in=None):
        self.id = key
        self.tag = tag
        self.weight = weight
        self.visited = visited
        self.info = info
        self.pos = pos
        self.edges_out = {}
        self.edges_in = {}

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{:d}".format(self.id)

    def __eq__(self, other):
        return self.id is other.id

    def __hash__(self):
        return hash(self.id)


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.vertices = {}
        self.ed_size = 0

    def v_size(self) -> int:
        return len(self.vertices)

    def e_size(self) -> int:
        return self.ed_size

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (not (id1 in self.vertices)) or (not (id2 in self.vertices)):
            return False

        if id1 == id2:
            return False

        n1 = self.vertices.get(id1)
        n2 = self.vertices.get(id2)

        if n1.edges_out.get(n2) is None:
            self.ed_size += 1
            self.mc += 1

        elif n1.edges_out.get(n2) is not weight:
            self.mc += 1

        n1.edges_out.update({n2: weight})
        n2.edges_in.update({n1: weight})
        return True

    def get_all_v(self) -> dict:
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.get_all_v().get(id1).edges_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.vertices.get(id1).edges_out

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.vertices.get(node_id) is not None:
            return False
        n1 = NodeData(key=node_id, pos=pos)
        self.vertices.update({node_id: n1})
        return True

    def remove_node(self, node_id: int) -> bool:
        n1 = self.vertices.get(node_id)
        if n1 is None:
            return False

        if n1.edges_out is not None:
            for n2 in n1.edges_out.keys:
                n2.edges_in.pop(n1)

        if n2.edges_in is not None:
            for n1 in n2.edges_in.keys:
                n1.edges_out.pop(n2)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        n1 = self.vertices.get(node_id1)
        n2 = self.vertices.get(node_id2)
        if n1 is None or n2 is None:
            return False
        if n1.edges_out.get(n2) is None:
            return False

        n1.edges_out.pop(n2)
        n2.edges_in.pop(n1)
        return True

    def __eq__(self, other):
        sorted(self.vertices)
        sorted(other.vertices)
        return self.vertices.__eq__(other.vertices) and other.vertices.__eq__(self.vertices)

    def __repr__(self):
        return str(self)

    def __str__(self):
        graph_str = "Graph: Vertices size: {:d} , Edges size: {:d}\n\t".format(self.v_size(), self.e_size())
        graph_str += '   Vertices: '
        for key in self.vertices.keys():
            graph_str += '{} '.format(key)
        graph_str += "\n\t   Edges: "
        for node1 in self.vertices.keys():
            n = self.vertices.get(node1)
            for dict1 in n.edges_out.keys():
                graph_str += str(node1)
                graph_str += '->'
                graph_str += ('{}: {} \t '.format(dict1, n.edges_out[dict1]))
        return graph_str
