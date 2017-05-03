import matplotlib.pyplot as plt
import networkx as nx

"""
This module demonstrates simple examples of network analysis
using pythons networkx library
"""
#Graph
G = nx.Graph()

#Nodes may be of different types
G.add_node(1)
nodelist= ["A", "B", "C", "D"]
G.add_nodes_from(nodelist)
G.remove_nodes_from(nodelist[2:])

#Edges: Nodes eg. "4" and "Z" can be added implicitly by adding an egde for them
G.add_edge("A", "B")
edgelist= [(1,"A"),(1,2),(1,4),(1,5),(2,"C"),("A", "Z")]
G.add_edges_from(edgelist)
G.remove_edges_from(edgelist[1:2])

#Degrees of nodes are stored in a dictionary {(NodeID:Degree)}
print("All nodes' degrees as a dict: ", G.degree(), "\nDegree of node A as an int: ", G.degree("A"))


"""
Visualizing graphs
networkx contains some empirical datasets one of which "karate_club_graph"
is used in this example
"""

KG= nx.karate_club_graph()
nx.draw(KG, with_labels=True, node_color="lightblue", edge_color="grey")
plt.savefig("./network_plots/karate_graph.pdf")