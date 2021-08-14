from __future__ import division
import networkx as nx


G= nx.Graph()
graph_num=1
probab=0.03
f_out= open("central_2hop_100_%s.txt"%probab ,"w+")

while graph_num<=10:
	
	f = open('100_%s_%s.txt' %(probab,graph_num))

	edgelist = []

	for line in f:
		coms= line.split()
		v1= int(coms[0])
		v2= int(coms[1])

		edgelist.append((v1,v2))

	G.add_edges_from(edgelist)

	highest_dcentrality = 0
	dselected_nodes = 0

	highest_bcentrality = 0
	bselected_nodes = 0

	highest_ccentrality = 0
	cselected_nodes = 0

	for i in range(100):
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
		if total_dcentrality/dtot_nodes>=highest_dcentrality:
			highest_dcentrality=total_dcentrality/dtot_nodes
			dselected_nodes=i

		selected_nodes = []
		total_bcentrality=0
		ltotal_bcentrality=[v for k, v in (nx.betweenness_centrality(G)).items() if k == i]
		total_bcentrality+=ltotal_bcentrality[0]
		btot_nodes=1
		selected_nodes.append(i)
		for j in G[i]:
			if j not in selected_nodes:
				ltotal_bcentrality=[v for k, v in (nx.betweenness_centrality(G)).items() if k == j]
				total_bcentrality+=ltotal_bcentrality[0]
				btot_nodes+=1
				selected_nodes.append(j)
				for m in G[j]:
					if m not in selected_nodes:
						ltotal_bcentrality=[v for k, v in (nx.betweenness_centrality(G)).items() if k == m]
						total_bcentrality+=ltotal_bcentrality[0]
						btot_nodes+=1
		if total_bcentrality/btot_nodes>=highest_bcentrality:
			highest_bcentrality=total_bcentrality/btot_nodes
			bselected_nodes=i

		selected_nodes = []
		total_ccentrality=0
		ltotal_ccentrality=[v for k, v in (nx.closeness_centrality(G)).items() if k == i]
		total_ccentrality+=ltotal_ccentrality[0]
		ctot_nodes=1
		selected_nodes.append(i)
		for j in G[i]:
			if j not in selected_nodes:
				ltotal_ccentrality=[v for k, v in (nx.closeness_centrality(G)).items() if k == j]
				total_ccentrality+=ltotal_ccentrality[0]
				ctot_nodes+=1
				selected_nodes.append(j)
				for m in G[j]:
					if m not in selected_nodes:
						ltotal_ccentrality=[v for k, v in (nx.closeness_centrality(G)).items() if k == m]
						total_ccentrality+=ltotal_ccentrality[0]
						ctot_nodes+=1
		if total_ccentrality/ctot_nodes>=highest_ccentrality:
			highest_ccentrality=total_ccentrality/ctot_nodes
			cselected_nodes=i

		print graph_num, i
	
	'''dselected_nodes.remove(0)	
	bselected_nodes.remove(0)	
	cselected_nodes.remove(0)'''	

	degcen = ("Degree Centrality", dselected_nodes, highest_dcentrality)
	betcen = ("Betweenness Centrality", bselected_nodes, highest_bcentrality)
	clocen = ("Closeness Centrality", cselected_nodes, highest_ccentrality)

	f_out.write("Graph %s \n" %graph_num)
	f_out.write(str(degcen)+"\n")
	f_out.write(str(betcen)+"\n")
	f_out.write(str(clocen)+"\n")
	f_out.write("\n\n")
	graph_num+=1
