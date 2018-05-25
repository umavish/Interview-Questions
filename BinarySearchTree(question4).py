# A Binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to find LCA of n1 and n2. Assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root.data
 
# Construct the BST from matrix.
# Root has to be given to build BST
def createTree(mat,root):
	node_value = 0
	for elem in mat[root.data]:
		#print elem
		if elem:
			if (node_value < root.data):
				root.left = Node(node_value)
			else:
				root.right = Node(node_value)
		node_value = node_value+1
	if (root.left != None):
		createTree(mat, root.left)
	if (root.right != None):
		createTree(mat, root.right)	
	
# Creates BST by calling createTree and calls lca function
# to find least common ancestor of nodes n1,n2
def question4(T, r, n1, n2):
	root = Node(r)
	createTree(T,root)
	return lca(root, n1, n2)
		
# Test case
print question4([[0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1],
                     [0, 0, 0, 0, 0]],
                     3, 4, 3)		
                     

