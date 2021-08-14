import networkx as nx

G= nx.Graph()
graph_num=1
probab=0.05
f_out= open("central100_%s.txt"%probab ,"w+")

while graph_num<=10:
	f = open('100_%s_%s.txt' %(probab,graph_num))

	edgelist = []

	for line in f:
		coms= line.split()
		v1= int(coms[0])
		v2= int(coms[1])
	
		edgelist.append((v1,v2))

	G.add_edges_from(edgelist)

	highest_d = max((nx.degree_centrality(G)).values())
	f_out.write("Highest Degree Centrality of graph %s:"%graph_num+str([k for k, v in (nx.degree_centrality(G)).items() if v == highest_d]))

	highest_b = max((nx.betweenness_centrality(G)).values())
	f_out.write("\nHighest Betweenness Centrality of graph %s:"%graph_num+str([k for k, v in (nx.betweenness_centrality(G)).items() if v == highest_b]))

	highest_c = max((nx.closeness_centrality(G)).values())
	f_out.write("\nHighest Closeness Centrality of graph %s:"%graph_num+str([k for k, v in (nx.closeness_centrality(G)).items() if v == highest_c])+"\n\n")

	graph_num+=1
