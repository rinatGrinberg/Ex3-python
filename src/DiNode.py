import random


class DiNode:

    def __init__(self, key, pos: tuple, tag=0, info=""):

        self.id = key
        self.pos = pos
        self.tag = tag
        self.info = info

        self.ins = {}    # all in edges <node_key : weight>
        self.outs = {}   # all out edges <node_key : weight>

        if self.pos is None:
            x, y, z = random.uniform(0, 10), random.uniform(0, 10), 0
            self.pos = (x, y, z)

    def __repr__(self):
        return f"{self.id} "
