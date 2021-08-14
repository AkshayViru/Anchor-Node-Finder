from __future__ import division
import networkx as nx


graph_num=1
probab=0.03
f_out= open("central1d.txt" ,"w+")
anchor_list=[49,30,90,85,83,3,77,48,54,69]

while graph_num<=10:

	print graph_num
	G= nx.Graph()

	f = open('100_%s_%s.txt' %(probab,graph_num))

	edgelist = []

	for line in f:
		coms= line.split()
		v1= int(coms[0])
		v2= int(coms[1])

		edgelist.append((v1,v2))

	G.add_edges_from(edgelist)
	'''anc_dcentrality=[v for k, v in (nx.degree_centrality(G)).items() if k == anchor_list[0]]
	print anchor_list[0], anc_dcentrality
	del anchor_list[0]'''

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

	highest_ncent=0
	highest_node=[]

	for i in range(100):

		ltotal_ncent=[v for k, v in (nx.degree_centrality(G)).items() if k == i]		
		total_ncent=ltotal_ncent[0]
		
		if total_ncent>highest_ncent:
			highest_ncent=total_ncent
			highest_node.append((i, total_ncent))

		total_dcentrality=0
		selected_nodes = [i]	
		for j in G[i]:
			selected_nodes.append(j)
		selected_nodes=remove_duplicates(selected_nodes)
		for j in selected_nodes:
			ltotal_dcentrality=[v for k, v in (nx.degree_centrality(G)).items() if k == j]		
			total_dcentrality+=ltotal_dcentrality[0]

		avg_dcentrality=total_dcentrality/len(selected_nodes)


		if avg_dcentrality>=highest_dcentrality:
			highest_dcentrality=avg_dcentrality
			dselected_nodes.append((i,highest_dcentrality))

	print highest_node
	for x,y in dselected_nodes:
		if y==highest_dcentrality:
			final_nodes.append(x)

	graph_num+=1
	degcen = (final_nodes, highest_dcentrality)
	f_out.write(str(degcen)+"\n")
	
