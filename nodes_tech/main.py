from flask import Flask, render_template, jsonify

from gen_nodes import *
from Node_mgmt import *


app = Flask(__name__)

plane = gen_nodes()

@app.route('/')
def index():
    return render_template('nodes.html', nodes=plane.world)

@app.route('/get_nodes')
def get_nodes():
    return jsonify([{"id": node.id,
                     "correlates" : node.correlates,
                     "name": node.name,
                     "size": node.size,
                     "type": node.type.name } for node in plane.world])

if __name__ == '__main__':
    app.run(debug=True)