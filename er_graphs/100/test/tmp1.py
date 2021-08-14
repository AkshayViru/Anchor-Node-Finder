from __future__ import division
import networkx as nx


G= nx.Graph()

edgelist=[(0,4),(0,5),(3,5),(1,4),(4,7),(9,7),(9,6),(2,6),(2,8)]

G.add_edges_from(edgelist)

print G.edges()

print nx.degree_centrality(G)

highest_dcentrality = 0
dneighboring_nodes = 0
dselected_nodes = []

for i in range(10):
		selected_nodes = []
		total_dcentrality=0
		ltotal_dcentrality=[v for k, v in (nx.degree_centrality(G)).items() if k == i]
		total_dcentrality+=ltotal_dcentrality[0]
		dtot_nodes=1
		selected_nodes.append(i)
		for j in G[i]:
			if j not in selected_nodes:
				ltotal_dcentrality=[v for k, v in (nx.degree_centrality(G)).items() if k == j]
				total_dcentrality+=ltotal_dcentrality[0]
				dtot_nodes+=1
				selected_nodes.append(j)
				for m in G[j]:
					if m not in selected_nodes:
						ltotal_dcentrality=[v for k, v in (nx.degree_centrality(G)).items() if k == m]
						total_dcentrality+=ltotal_dcentrality[0]
						dtot_nodes+=1
		if total_dcentrality>=highest_dcentrality:
			highest_dcentrality=total_dcentrality
			dneighboring_nodes=dtot_nodes
			dselected_nodes.append(i)
		print i, total_dcentrality

dselected_nodes.remove(0)
degcen = ("Degree Centrality", dselected_nodes, highest_dcentrality/dneighboring_nodes)
print degcen
