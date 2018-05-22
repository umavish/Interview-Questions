def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)
    
    
def question1(s,t):

    # Defining local variables.
    t_len = len(t)
    print t_len
    s_len = len(s)
    t_sort = sorted(t)

    # Setting the range to be that of t.
    for i in range(len(s) - len(t) + 1):
       

        # Call helper function which checks for t in s.
        if is_anagram(s[i: i+len(t)], t):
            return True
    return False

# Simple test case.
print question1("udacity", "")
# True



