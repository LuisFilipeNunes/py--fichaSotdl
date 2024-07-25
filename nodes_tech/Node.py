from TypeNodes import TypeNodes

class Node:
    def __init__(self, id: int, name: str, type: TypeNodes):
        self.id = id
        self.correlates = []
        self.name = name
        self.size = 0
        self.type = type

    def add_correlation(self, node_id: int):
        if node_id == self.id:
            return
        if node_id not in self.correlates:
            self.correlates.append(node_id)
            self.size = len(self.correlates)

    def remove_correlation(self, node_id: int):
        if node_id in self.correlates:
            self.correlates.remove(node_id)
            self.size = len(self.correlates)

    def get_id(self):
        return self.id

    def get_correlates(self):
        return self.correlates

    def get_size(self):
        return self.size
