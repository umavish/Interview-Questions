
# Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
from collections import defaultdict
def find(parent, i):
		
	if parent[i] == i:
		return i
	return find(parent, parent[i])
 
# A function that does union of two sets of x and y
# (uses union by rank)
def union(parent, rank, x, y):
	xroot = find(parent, x)
	yroot = find(parent, y)
		
 
# Attach smaller rank tree under root of 
# high rank tree (Union by Rank)
	if rank[xroot] < rank[yroot]:
		parent[xroot] = yroot
	elif rank[xroot] > rank[yroot]:
		parent[yroot] = xroot
		
 # If ranks are same, then make one as root 
# and increment its rank by one
	else :
		parent[yroot] = xroot
		rank[xroot] += 1
		
 
# The main function to construct MST using Kruskal's algorithm
def KruskalMST(graph, V):
 
	result =[] #This will store the resultant MST
 
	i = 0 # An index variable, used for sorted edges
	e = 0 # An index variable, used for result[]
 
    # Step 1:  Sort all the edges in non-decreasing 
              
	graph =  sorted(graph,key=lambda item: item[2])
 
	parent = [] ; rank = []
 
    # Create V subsets with single elements
	for node in range(V):
		parent.append(node)
		rank.append(0)
		
     
    # Number of edges to be taken is equal to V-1
	while e < V -1 :
 
        # Step 2: Pick the smallest edge and increment 
                    # the index for next iteration
		u,v,w =  graph[i]
		i = i + 1
		x = find(parent, u)
		y = find(parent ,v)
 
        # If including this edge does't cause cycle, 
                        # include it in result and increment the index
                        # of result for next edge
		if x != y:
			e = e + 1    
			result.append([u,v,w])
			union(parent, rank, x, y)            
        # Else discard the edge
 
    # print the contents of result[] to display the built MST
	
	final_result = defaultdict(list)
	for u,v,w in result:
		final_result[n_l(u)].append((n_l(v),w))  
	return final_result
			
		
def question3(s1):
	V=len(s1)
	graph = []
	for key, value in s1.iteritems():
		for i in value:
			u,v,w = l_n(key), l_n(i[0]), i[1]
			graph.append([u,v,w]) 
	return KruskalMST(graph, V)
			 
def l_n(letter):
    return ord(letter.lower()) - 97
    
def n_l(number):
	return chr(number+65)
 

s1 = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}

print question3(s1)

