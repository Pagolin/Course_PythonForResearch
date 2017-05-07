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

#plt.figure()
#for i in range(3):
#    GI= generate_ER_graph(500, 0.08)
#    plot_degree_distribution(GI)
#plt.savefig("./network_plots/many_degree_distributions.pdf")

"""
Descriptive Statistics of social networks
"""
import numpy as np

#Import Adjacency matrices discribing the social relation in two indian villages
A1= np.loadtxt("./network_data/adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2= np.loadtxt("./network_data/adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)
G1.degree().values()

def basic_net_stats(G):
    print("Number of nodes: %d" %G.number_of_nodes())
    print("Number of edges: %d" %G.number_of_edges())
    print("Mean node degrees: %.2f" %np.mean(list(G.degree().values())))

basic_net_stats(G1)
basic_net_stats(G2)
plt.figure()
plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.show()
#Conclusion => ER graphs are not an appropriate approximation to social network graphs

"""
Find connected components in graphs 
Generator functions: Networkx function connected_component_subgraph() doesn't create a data object but a generator object, that can be used to create a series of objects using the next()  function (like a "productive iterator").
"""
generator = nx.connected_component_subgraphs(G1)
component = generator.__next__()
nr_of_nodes = len(generator.__next__())
print("Produced a subgraph with %d Nodes, next subgraph will have %d Nodes" %(component.number_of_nodes(), nr_of_nodes))

#Find the largest conected component

gen = nx.connected_component_subgraphs(G1)
G1_largest_connected_component = max(nx.connected_component_subgraphs(G1), key = len)
G2_largest_connected_component= max(nx.connected_component_subgraphs(G2), key = len)
print("Largest components have %d and %d Nodes in G1 and G2, respectively" %(len(G1_largest_connected_component), len(G2_largest_connected_component)))

"""
Visualize components
By default nx.draw plots the graphs stochastically, altering the appearance of each graph slightly in every single call.
However general tendencies, as the ovious partition of G2s largest subset into two, connected subgroups are present in every vizualisation
"""
plt.figure()
nx.draw(G1_largest_connected_component, node_color= "blue", edge_color= "darkgrey", nodesize=3)
plt.savefig("./network_plots/largest_component_village1.pdf")
plt.figure()
nx.draw(G2_largest_connected_component, node_color= "blue", edge_color= "darkgrey", nodesize=3)
plt.savefig("./network_plots/largest_component_village2.pdf")





