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
if len (sys.argv) != 2 :
    print "Enter arguments in this format: arg1=size of grid"
    sys.exit (1)

tmp1= map(int, sys.argv[1:])
limit = tmp1[0]


#generates a grid of size specified by the argument
G = nx.grid_graph(dim=[limit,limit], periodic=False)


for i in range(limit):
	G.add_edge((i,0),(i,limit-1))


for i in range(limit*limit):
	print i

for j in G.edges():
	print j
