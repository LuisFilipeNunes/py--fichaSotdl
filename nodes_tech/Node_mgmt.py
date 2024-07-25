from Node import Node


class Node_mgmt():

    def __init__(self, id: int, name: str):
        self.id = id
        self.world = []
        self.name = name
        self.size = 0

    def add_node(self, node):
        self.world.append(node)
        self.size = len(self.world)
    
    def remove_node(self, node):
        if node in self.world:
            self.world.remove(node)
            self.size = len(self.world)
    
    def get_node(self, node_id, node_name=None):
        for node in self.world:
            if node_name is not None and node.name == node_name:
                return node
            if node.get_id() == node_id:
                return node
        return None
    
    def make_correlation(self, node1, node2):
        self.get_node(node1).add_correlation(node2)
        self.get_node(node2).add_correlation(node1)