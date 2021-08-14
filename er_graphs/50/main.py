import networkx as nx
import sys
import itertools
from multiprocessing import Process, Queue
import re

if len (sys.argv) != 2 :
    print "Enter arguments in this format: probabilty"
    sys.exit (1)

tmp1= map(float, sys.argv[1:])
probab = tmp1[0]

graph_count=9

while graph_count<=10:

	found=False
	ll_reqd=1
	limit=50
	details=[]

	f_out= open("50_%s_%sResult.txt"%(probab,graph_count),"w+")

	while found==False:
		G= nx.erdos_renyi_graph(limit, probab)

		if nx.is_connected(G):
			f_in= open("50_%s_%s.txt"%(probab, graph_count),"w+")
			nx.write_edgelist(G,"50_%s_%s.txt"%(probab, graph_count),data=False)

			found=True

	details.append(("..","..",nx.average_shortest_path_length(G)))

	def f(l1,l2, q):
		
		distance=nx.average_shortest_path_length(G)
		for i in range(limit):
			for j in range(l1,l2):	
				#if loop to prevent self loops and multilinks
				if j not in G[i] and j!=i:
					G.add_edge(i, j)
					newdistance= nx.average_shortest_path_length(G)
					G.remove_edge(i, j)
					if newdistance<distance:
						distance= newdistance
						node1=i
						node2=j
		q.put((distance, node1, node2))
	

	while ll_reqd<=25:
		if __name__ == '__main__':
			q = Queue()
		
			p1 = Process(target=f, args=(0, limit/4, q))
			p1.start()
			p2 = Process(target=f, args=(limit/4, limit/2, q))
			p2.start()
			p3 = Process(target=f, args=(limit/2, 3*limit/4, q))
			p3.start()
			p4 = Process(target=f, args=(3*limit/4, limit, q))
			p4.start()
	
			min_d = 100
			count = 0

			while count<4:
				cur_d, n1, n2= q.get()
				if cur_d<min_d:
					min_d=cur_d
					node1=n1
					node2=n2
				count+=1
			print (graph_count, ll_reqd, min_d, node1, node2)
			G.add_edge(node1, node2)
			details.append((node1, node2, min_d))
		
			p1.join()
			p2.join()
			p3.join()
			p4.join()

			ll_reqd +=1

	for i in range(len(details)):
		datam=str(details[i])
		datam = re.sub('[^A-Za-z0-9\.]+', ' ', datam)
		f_out.write(datam)
		f_out.write("\n")
		

	f_in.close()
	f_out.close()

	graph_count+=1
