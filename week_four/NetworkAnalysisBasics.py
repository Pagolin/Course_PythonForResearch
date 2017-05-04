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


"""
Random Graph Models
Comparable to sampling numbers from a given distribution (e.g. normal or bionamial distributions), graphs can be sampled 
randomly from a collection of random graphs.
The simplest of such "random graph models" is the Erdős–Rényi model:
ER graph model with: 
N - Number of Nodes
p - Probability of any pair of nodes to be connected
--> p==1 => complete graph
Task: Implement an ER- model
"""
from scipy.stats import bernoulli

#Generate a single Bernoulli random variable, with p=> probalbility of 1 (1-p => probability of 0)
bernoulli.rvs(p=0.2)

#Create a random graph by hand
N=20
p=0.2
def generate_ER_graph(Nr, prob):
    """
    Takes a number of Nodes and a general probability for two nodes to be connected and returns a random graph (Erdős–Rényi graph)
    :param Nr: Number of nodes
    :param prob: probability range=[0,1] 
    :return: Graph with Nr nodes and random edges
    """
    G=nx.Graph()
    G.add_nodes_from(range(Nr))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=prob):
                G.add_edge(node1, node2)
    return G
G2 = generate_ER_graph(N, p)

plt.figure()
nx.draw(G2, with_labels=True, node_color="green", edge_color="black")
plt.savefig("./network_plots/ER_graph.pdf")

"""
Plotting the degree distribution
"""

def plot_degree_distribution(G):
    #!!Caution!!: G.degree().values() returns a view object
    # Make shure to turn it into another type (eg list) to prevent unwanted manipulation of the graph
    degrees= list(G.degree().values())
    plt.hist(degrees, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

G3 = generate_ER_graph(500, 0.08)
plt.figure()
plot_degree_distribution(G3)
plt.savefig("./network_plots/degree_distribution.pdf")

plt.figure()
for i in range(3):
    GI= generate_ER_graph(500, 0.08)
    plot_degree_distribution(GI)
plt.savefig("./network_plots/many_degree_distributions.pdf")