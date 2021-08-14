import networkx as nx
import matplotlib.pyplot as plt

f=False
while f==False:
	G= nx.erdos_renyi_graph(100,0.04)
	if nx.is_connected(G):
		f=True
		nx.draw(G, with_labels=True)
		
plt.show()
