from Node import Node
from TypeNodes import TypeNodes
from Node_mgmt import Node_mgmt
import random
import string

def generate_random_name(length=5):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_nodes(num_nodes):
    plane = Node_mgmt(1, "teste")
    for i in range(num_nodes):
        name = generate_random_name()
        node_type = random.choice(list(TypeNodes))        
        plane.add_node(Node(i, name, node_type))
    
    return plane

def gen_nodes():
    num_nodes = 6  # You can change this to any number you want
    generated_plane = generate_nodes(num_nodes)
    
    for node in generated_plane.world:
        generated_plane.make_correlation(random.choice(generated_plane.world).get_id(), node.get_id())
        flag = random.randint(0, 1)
        while flag == 0:
            generated_plane.make_correlation(random.choice(generated_plane.world).get_id(), node.get_id())
            flag = random.randint(0, 1)

    return generated_plane


