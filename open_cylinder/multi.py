import networkx as nx
import matplotlib.pyplot as plt
import itertools
import sys
from multiprocessing import Process, Queue
import xlsxwriter
import time

start_time = time.time()

#for command line arguments
if len (sys.argv) != 3 :
    print "Enter arguments in this format: arg1=size of 2D grid, arg2: no of links"
    sys.exit (1)

tmp1= map(int, sys.argv[1:])
size = tmp1[0]

tmp2= map(int, sys.argv[2:])
links_to_add = tmp2[0]

G=nx.Graph()

def make_graph(size):
	G = nx.grid_graph(dim=[size,size], periodic=False)

	for i in range(size):
		G.add_edge((i,0),(i,size-1))

	return G


def possible_lls(G):
	possible_ll = []
	for x,y in itertools.product(range(size), range(size)):
		for i,j in itertools.product(range(size), range(size)):
			if (i,j) not in G[(x,y)] and (i,j)!=(x,y):
				possible_ll.append(((x,y),(i,j)))
	return possible_ll	

def get_apl(ll,q):
	min_values=()
	distance=nx.average_shortest_path_length(G)
	for x,y in ll:
		if (x,y) not in G.edges():
			G.add_edge(x,y)
			new_distance=nx.average_shortest_path_length(G)
			G.remove_edge(x,y)
			if new_distance<distance:
				distance=new_distance
				min_values=(new_distance,x,y)
	q.put(min_values)

def split_List():
	#split possible ll into 4 parts
	llno=len(possible_ll)
	n=llno/4
	llist=[]
	for i in range(0, llno, n):
		llist.append(possible_ll[i:i + n])
	return llist

def make_excel(NodeList, APLlist):
	#for excel sheet
	NodeList=list(itertools.chain.from_iterable(NodeList))

	firstNodes=NodeList[::2]
	firstNodes = [str(t) for t in firstNodes]
	secondNodes=NodeList[1::2]
	secondNodes = [str(t) for t in secondNodes]

	#to store data to be passed to Excel
	total=();

	for i in range(0, links_to_add+1):
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

G=make_graph(size)
possible_ll=possible_lls(G)
llist=split_List() 

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Sheet-%sby%sby%s.xlsx' %(size,size,size))
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

distance=nx.average_shortest_path_length(G)

APLlist=[distance]
NodeList=[("-","-")]

links_added=0
while links_added<links_to_add:
	q = Queue()
	
	p1 = Process(target=get_apl, args=(llist[0], q))
	p1.start()
	p2 = Process(target=get_apl, args=(llist[1], q))
	p2.start()
	p3 = Process(target=get_apl, args=(llist[2], q))
	p3.start()
	p4 = Process(target=get_apl, args=(llist[3], q))
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
	print (links_added+1+min_d, node1, node2)
	G.add_edge(node1, node2)
	
	NodeList.append((node1, node2))
	APLlist.append(min_d)

	links_added+=1
		
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	
make_excel(NodeList, APLlist)
#nx.draw(G, with_labels=True)
#plt.show()
print("--- %s seconds ---" % (time.time() - start_time))
