from __future__ import division
import networkx as nx


G= nx.Graph()
graph_num=1
probab=0.03
f_out= open("central_2hop_100_%s.txt"%probab ,"w+")

while graph_num<=2:
	print graph_num
	f = open('100_%s_%s.txt' %(probab,graph_num))

	edgelist = []

	for line in f:
		coms= line.split()
		v1= int(coms[0])
		v2= int(coms[1])

		edgelist.append((v1,v2))

	G.add_edges_from(edgelist)

	highest_dcentrality = 0
	dneighboring_nodes = 0
	dselected_nodes = []

	highest_bcentrality = 0
	bneighboring_nodes = 0
	bselected_nodes = []

	highest_ccentrality = 0
	cneighboring_nodes = 0
	cselected_nodes = []

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
		if total_dcentrality>highest_dcentrality:
			highest_dcentrality=total_dcentrality
			dneighboring_nodes=dtot_nodes
			dselected_nodes.append(i)

		total_bcentrality=0
		ltotal_bcentrality=[v for k, v in (nx.betweenness_centrality(G)).items() if k == i]
		total_bcentrality+=ltotal_bcentrality[0]
		btot_nodes=1
		for j in G[i]:
			ltotal_bcentrality=[v for k, v in (nx.betweenness_centrality(G)).items() if k == j]
			total_bcentrality+=ltotal_bcentrality[0]
			btot_nodes+=1
			for m in G[j]:
				ltotal_bcentrality=[v for k, v in (nx.betweenness_centrality(G)).items() if k == m]
				total_bcentrality+=ltotal_bcentrality[0]
				btot_nodes+=1
		if total_bcentrality>highest_bcentrality:
			highest_bcentrality=total_bcentrality
			bneighboring_nodes=btot_nodes
			bselected_nodes.append(i)

		total_ccentrality=0
		ltotal_ccentrality=[v for k, v in (nx.closeness_centrality(G)).items() if k == i]
		total_ccentrality+=ltotal_ccentrality[0]
		ctot_nodes=1
		for j in G[i]:
			ltotal_ccentrality=[v for k, v in (nx.closeness_centrality(G)).items() if k == j]
			total_ccentrality+=ltotal_ccentrality[0]
			ctot_nodes+=1
			for m in G[j]:
				ltotal_ccentrality=[v for k, v in (nx.closeness_centrality(G)).items() if k == m]
				total_ccentrality+=ltotal_ccentrality[0]
				ctot_nodes+=1
		if total_ccentrality>highest_ccentrality:
			highest_ccentrality=total_ccentrality
			cneighboring_nodes=ctot_nodes
			cselected_nodes.append(i)

		print i
		
	degcen = ("Degree Centrality", dselected_node, highest_dcentrality/dneighboring_nodes)
	betcen = ("Betweenness Centrality", bselected_node, highest_bcentrality/bneighboring_nodes)
	clocen = ("Closeness Centrality", cselected_node, highest_ccentrality/cneighboring_nodes)

	f_out.write("Graph %s" %graph_num)
	f_out.write(str(degcen))
	f_out.write(str(betcen))
	f_out.write(str(clocen))
	f_out.write("\n\n")
	graph_num+=1
