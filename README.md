# Anchor Nodes Detector
Contains the code for detecting anchor nodes in different types of networks which reduce the average path length of the network by maximum.

## 2-D GRID NETWORK:

### Code:
- The main.py can be used to generate N*N 2-D grid networks. It will also add the most optimum LL and calculate the APL. These data are stored in an Excel Sheet. 
- It can also be used to plot APL-LL graph and the degree distribution. It is possible to print the adjacency matrix that can be used to check whether the code is working properly or not. These parts are kept in comments as they are not essential for our work and can be used when necessary.
- Command line arguments are necessary for executing the program. The two arguments that must be provided are: size of the grid network, the number of LL to be added. Eg: to generate a `$4\times4$` grid network and add 20 LLs, the code can be executed as follows:
`python main.py 4 20`

### Dataset:
Anchor Node plots show the position of the anchor node in different grid networks. Eg: the figure 9grid.png shows that the position of anchor node in 9*9 grid network is at (1,4) if you consider the bottom-most row as row 0 and first column as column 0. 
APL_LL charts show the variation of APL with the addition of LL for different grid networks. Eg: APL-LL:4-8.png shows that the APL of a 4*4 grid network decreases from roughly about 2.67 when no LL are added to 1.85 when 8 LLs are added.
Degree Distributions folder contains the degree distribution, i.e. the count of different degree nodes, for various grid networks. Each folder contains the degree distribution of networks as more and more LL are added. For eg: the 5*5 folder contains the degree distribution of 5*5 grid network from the addition of 1 LL to 12 LLs.
LL with APL folder contains the Excel Sheets containing LL addition data for various grid networks. It contains the number of LL added, the nodes between which LL is added, and the value of APL after the addition of a particular LL. Two dat files are also present which contains the same data(for 20*20 and 25*25 grid networks), but here nodes are named as 0,1,2... rather than (0,0),(0,1),(0,2)...

## RANDOM GRAPHS:

### Code:
The main.py can be used to generate 10 random graphs with a given probability. It will also add the most optimum LL and calculate the APL. These data are stored in two txt files. First txt file contains the edgelist of the graph generated and the second txt file contains the LLs added along with the APL after their addition.
Only one command line argument needs to be provided, i.e. the probability of the random graph. For eg: to generate 10 random graphs with probability 0.04 the code can be executed as follows-
		`python main.py 0.04`
The number of nodes needed in the graph and the number of LLs to be added can be changed by changing the value of their respective variables in the code.
The centrality of graphs can be found be using the codes given in the centrality folder. The edgelist generated previously must be kept in the same folder as the centrality code. 
The highest_centrality.py is used to find the node with the highest degree centrality in the graph. Node with highest betweenness and closeness centrality centrality can be found using the same code by change nx.degree_centrality(G) in line 47 to whatever centrality the user wishes to use.
The 1_hop_highest_centrality.py is used to find the node with highest 1-hop regional centrality and similarly 2_hop_highest_centrality.py finds the node with highest 2-hop regional centrality. By default both these check for degree centrality. In 1_hop_highest_centrality.py, nx.degree_centrality(G) in line 55 can be changed to the required centrality and in 2_hop_highest_centrality.py the same can be changed in line 56.

### Dataset:
It contains the data generated for random graphs with 50 and 100 nodes. Within each folder, contains various folders which are classified based on the probability used.
Two txt files are present for each graph as told earlier. Apart from this, centrality folder contains the nodes with highest centrality. 
The centrality files have been named in this format: centralHF.txt where H can be 0,1, or 2 - 0 means no-hop, 1 means 1-hop and 2 means 2-hop. F denotes the type of centrality- b means betweenness, c means closeness, and d means degree centrality. 
Each centrality txt file contains the nodes with highest centrality and it's centrality value. The node is stored in a list as there can be chance that more than one node has highest centrality value.

## CYLINDRICAL NETWORKS:

### Code:
The code for open cylindrical network is mostly similar to the code for 2-D grid network. The only change is in that first column nodes are connected to last column nodes. When opposite nodes in first row and opposite nodes in last row are connected, we get the closed cylindrical network.
A multiprocessing program has also been added for open cylindrical network to speed things up. Four processes are created in the program. In some cases, main.py maybe faster than multi.py.
The arguments are same as that for 2-D grid network- the network size and number of LL to be added. 

### Dataset:
Anchor node plots show the position of anchor node in the network for various networks. It is similar to plots seen earlier.
LL with APL Sheets are excel and txt files that contains the details regarding the nodes between which LLs are added and the corresponding APL that we get.

