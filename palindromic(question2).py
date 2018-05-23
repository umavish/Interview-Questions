
# Gives substrings of s in decending order.
def substring(s):
	
	# Here I chose range over xrange for python version compatibility.
	
	for end in range(len(s), 0, -1):
		 
		for start in range(len(s)-end+1):
			
			yield s[start: start+end]

# Define palindrome.
def is_palindrome(s):
	
	return s == s[::-1]

# Main function.
def question2(a):
    for l in substring(a):
		print l
		
		if is_palindrome(l):
			return l

# Simple test case.
print question2("mmaromadtpa")
# madam
