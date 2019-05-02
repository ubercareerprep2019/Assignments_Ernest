#This function takes two strings and returns true if one string is a permutation of
#the other, false otherwise.
def isStringPermutation(s1, s2):
    #check for if string are not equal in length this results in faster run time in somecases
    if(len(s1) != len(s2)):
        return False
    # sorted() python function used to lexicographical order strings
    # to handle case sensitive strings use python .lower() function
    sortedS1 = sorted(s1.lower())
    sortedS2 = sorted(s2.lower())
    #compared
    if (sortedS1 == sortedS2):
        return True
    else:
        return False
# worstcase runtime is O(nlogn)
print(isStringPermutation("Ernest", "nester"))
