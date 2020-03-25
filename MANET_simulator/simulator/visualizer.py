import cv2
import numpy as np


def step(net, t, dynamic, sim_time = 1000):
    """
        Updates the visualizer in each time step.
        Args:
            net: Graph of the network
            sim_time: Time interval between updates
    """
    img = np.ones((1000, 1000, 3), dtype=np.uint8) * 255
    pkts = net.step(t, dynamic)
    pkt_colors = {'REQ': (255, 255, 0), 'REP': (255, 0, 255), 'DATA': (0, 255, 255)}
    print(pkts)
    for n in net.nodes:
        cv2.circle(img, (n.x, n.y), 5, (255, 0, 0), thickness=20)
        cv2.putText(img, n.id, (n.x, n.y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
        cv2.circle(img, (n.x, n.y), n.range, (0, 255, 0), thickness=2)
        for adj in n.adjacent_nodes.keys():
            adj_node = n.adjacent_nodes[adj]
            cv2.line(img, (n.x, n.y), (adj_node.x, adj_node.y), (0, 0, 255), 3)
        img2 = img.copy()
        for pkt in pkts:
            n1 = net.nodes[int(pkt[0])]
            n2 = net.nodes[int(pkt[1])]
            pkt_type = pkt[2]
            cv2.line(img2, (n1.x, n1.y), (n2.x, n2.y), pkt_colors[pkt_type], 10)
            cv2.putText(img2, "{} :{}".format(pkt_type,pkt[3]), (int((n1.x+n2.x)/2), int((n1.y+n2.y)/2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
    cv2.imshow('vis', img)
    cv2.waitKey(sim_time)
    cv2.imshow('vis', img2)
    cv2.waitKey(sim_time)
    cv2.imshow('vis', img)
    cv2.waitKey(sim_time)


