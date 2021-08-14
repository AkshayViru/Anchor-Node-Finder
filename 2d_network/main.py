import networkx as nx
import matplotlib.pyplot as plt
import itertools
import sys
import collections
import xlsxwriter
import os
import time

start_time = time.time()

#for command line arguments
if len (sys.argv) != 3 :
    print "Enter arguments in this format: arg1=size of grid, arg2: no of links"
    sys.exit (1)

tmp1= map(int, sys.argv[1:])
limit = tmp1[0]

tmp2= map(int, sys.argv[2:])
llno = tmp2[0]

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Sheet-%sby%s.xlsx' %(limit,limit))
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

#to make sure only the possible number of LL can be added
#eg: in 2*2 grid network, only (4*3)/2-(2*2*1)= 2 links can be added more
#2*2*1 is the number of links already present

maxllpossible=(((limit*limit)*((limit*limit)-1))/2-(2*limit*(limit-1)))
if llno>maxllpossible:
	print "Number of links to be added must be less than ", maxllpossible+1
    	sys.exit (1)

#generates a grid of size specified by the argument
G = nx.grid_graph(dim=[limit,limit], periodic=False)

distance=nx.average_shortest_path_length(G)

nloops=1

#for APL-LL graph and ExcelSheet
APLlist=[distance]
LLlist=[0]

#for ExcelSheet
NodeList=[("-","-")]

while nloops<=llno:
	
	for x,y in itertools.product(range(limit), range(limit)):
			for i,j in itertools.product(range(x,limit), range(limit)):	
				#if loop to prevent self loops and multilinks
				if (i,j) not in G[(x,y)] and (i,j)!=(x,y):
					G.add_edge((x, y), (i, j))
					newdistance= nx.average_shortest_path_length(G)
					if newdistance<distance:
						distance= newdistance
						node1a=x
						node1b=y
						node2a=i
						node2b=j
					#removes the last added edge
					G.remove_edge((x, y), (i, j))

	print "minimum APL = ",distance, " node 1 =",(node1a, node1b), " node 2=" ,(node2a, node2b) 
	G.add_edge((node1a, node1b), (node2a, node2b))
	
	nloops+=1


	NodeList.append(((node1a, node1b), (node2a, node2b)))
	LLlist.append(nloops)
	APLlist.append(distance)


#for excel sheet
NodeList=list(itertools.chain.from_iterable(NodeList))

firstNodes=NodeList[::2]
firstNodes = [str(t) for t in firstNodes]
secondNodes=NodeList[1::2]
secondNodes = [str(t) for t in secondNodes]

#to store data to be passed to Excel
total=();

for i in range(0, nloops):
	total += ([i, firstNodes[i], secondNodes[i], APLlist[i]],)


#Creates ExcelSheet

worksheet.set_column(0, 0, 12)
worksheet.set_column(3, 3, 12)

row = 1
col = 0

worksheet.write('A1', 'LL Number', bold)
worksheet.write('B1', 'Node 1', bold)
worksheet.write('C1', 'Node 2', bold)
worksheet.write('D1', 'APL Length', bold)

for num, node1, node2, apl in (total):
   	worksheet.write(row, col, num)
	worksheet.write(row, col+1, node1)
	worksheet.write(row, col+2, node2)
	worksheet.write(row, col+3, apl)  
   	row += 1

workbook.close()
'''

#can be used to check adjacency matrix, to confirm no multilinks or self loops are present

for s,t in itertools.product(range(limit), range(limit)):
	print "Adjacent nodes of ", s,t
	print G[(s,t)], "\n"


nx.draw(G, with_labels=True)
plt.show()


#plots APL-LL graph
plt.title('Relationship Between APL and LL')
plt.ylabel("APL")
plt.xlabel("LL")
plt.scatter(LLlist,APLlist)
plt.savefig("APL-LL:%s-%s.png" %(limit, llno), format="PNG")
#plt.show()
'''
#plots degree distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  
# degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Distribution")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.03 for d in deg])
ax.set_xticklabels(deg)

# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
pos = nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.4)

plt.savefig("%s-%s- Graph.png" %(limit, llno), format="PNG")
#plt.show()
'''
duration = 1  # second
freq = 440  # Hz
os.system('play --no-show-progress --null --channels 1 synth %s sine %f'% (duration, freq))
'''
print("--- %s seconds ---" % (time.time() - start_time))
