class Node:
  def __init__(self, name, id, type):
    self.__name = name
    self.__id = id
    self.__type = type
    self.__linked_nodes = []
    self.__size = 0
  
  def getName(self):
    return self.__name

  def set_name(self, new_name):
    self.__name = new_name
    
  def getId(self):
    return self.__id
  
  def set_Id(self, new_id):
    self.__id = new_id
  
  def get_type(self):
    return self.__type
  
  def set_type(self, new_type):
    self.__type = new_type
  
  def linkNewNode(self, new_node):
    self.__linked_nodes.append(new_node.getId())
    self.__size = len(self.__linked_nodes)
  
  def unlinkNode(self, node_id):
    self.__linked_nodes.remove(node_id)
    self.__size = len(self.__linked_nodes)
  
  def getLinkedNodes(self):
    return self.__linked_nodes
  
  def getSize(self):
    return self.__size
  
    
