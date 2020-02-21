f=open('/Users/Eyusd/Downloads/Math_Constants/Pi - Dec.txt')
#You can find the .txt here : https://pi2e.ch/blog/2017/03/10/pi-digits-download/#download
h=f.readlines()[0][1:]
import numpy as np
###


def search(n):
    ref = str(n)
    pathlist = [str(int(ref))]
    pathlist.append(str(h.find(pathlist[-1])))
    while (pathlist[-1] != ref) and (pathlist[-1] != pathlist[-2]):
        pathlist.append(str(h.find(pathlist[-1])))
    return pathlist

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def genGraph():
    G = nx.Graph()
    
    size =[i for i in range(1,1001)]
    G.add_nodes_from(size)
    for x in size:
        u = h.find(str(x))
        if 0< u < size[-1]:
            G.add_edge(x,u)
    numedges = G.number_of_edges()
    
    plt.figure(figsize=[30]*2)
    #remove = [node for node,degree in dict(G.degree()).items() if degree == 0]  #Remove this if you want to see all the nodes
    #G.remove_nodes_from(remove)
    nx.draw_circular(G,with_labels=True, node_size = 1, font_size=5, alpha = 0.5, font_color = 'black', node_color = 'black', edge_color=range(numedges), edge_cmap=plt.cm.plasma_r)
    plt.savefig("Pidec.png", dpi=400)
    return "Done"
