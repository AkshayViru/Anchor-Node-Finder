from __future__ import division
import networkx as nx


graph_num=1
probab=0.03
f_out= open("central2b.txt" ,"w+")

while graph_num<=10:
	G= nx.Graph()

	f = open('100_%s_%s.txt' %(probab,graph_num))

	edgelist = []

	for line in f:
		coms= line.split()
		v1= int(coms[0])
		v2= int(coms[1])

		edgelist.append((v1,v2))

	G.add_edges_from(edgelist)

	#removes duplicate list values
	def remove_duplicates(x):
	    z = [x[0]]
	    for i in range(1,len(x)):
		for y in range(0, i):
		    if x[i] == x[y]:
		        break
		else:
		    z.append(x[i])
	    return z   

	highest_dcentrality = 0
	dselected_nodes = []
	final_nodes=[]


	for i in range(100):
		print graph_num,i
		total_dcentrality=0
		selected_nodes = [i]	
		for j in G[i]:
			selected_nodes.append(j)
			for k in G[j]:
				selected_nodes.append(k)
		selected_nodes=remove_duplicates(selected_nodes)

		for j in selected_nodes:
			ltotal_dcentrality=[v for k, v in (nx.betweenness_centrality(G)).items() if k == j]
			total_dcentrality+=ltotal_dcentrality[0]

		avg_dcentrality=total_dcentrality/len(selected_nodes)

		if avg_dcentrality>=highest_dcentrality:
			highest_dcentrality=avg_dcentrality
			dselected_nodes.append((i,highest_dcentrality))

	for x,y in dselected_nodes:
		if y==highest_dcentrality:
			final_nodes.append(x)

	graph_num+=1
	degcen = (final_nodes, highest_dcentrality)
	f_out.write(str(degcen)+"\n")
	
