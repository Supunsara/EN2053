from simulator.graph import Graph
from simulator.visualizer import step
import cv2

manet = Graph()

# initialize network
"""
Make sure  the ranges of all nodes are the same to enable bidirectional 
communication so as to simplify the protocol
"""
tx_range = 200
dynamic = False  # True to use mobile model

manet.add_node(500, 550, tx_range)  # "Add node 0 at 500,500"
manet.add_node(690, 600, tx_range)  # "Add node 1 at 690,600"
manet.add_node(780, 700, tx_range)  # "Add node 2 at 780,700"
#
manet.send(0, 2, 4, 'Test')  # send a data packet at time step 5 from node 0 to 2
for t in range(10):  # Simulate for 10 time steps
    step(manet, t, dynamic)
cv2.destroyAllWindows()
