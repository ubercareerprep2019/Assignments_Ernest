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
    return sortedS1 == sortedS2
# worstcase runtime is O(nlogn)

def pairsThatEqualSum(inputArray,targetSum):
    answer = []
    for i in inputArray:
        if (targetSum-i in inputArray):
            inputArray.remove(i)
            answer.append([i, targetSum-i])
            #inputArray.remove(i)
    return answer
#worstcase runtime is O(n) or O(n^2) - becasue of if statement in for loop that has a python equivalent to .contains() check
#Method 1 Tests
print(isStringPermutation("helloErnest", "Helloernest"))
print(isStringPermutation("hello", "ehllo"))
print(isStringPermutation("dog", "cat"))
print(isStringPermutation("dogg", "dog"))
#Method 2 Tests
nums1 = [1,2,3,4,5,6,7,8,9]
nums2 = [1,2,3,4,5,6,7,8,9]
nums3 = [1,2,3,4,5,6,7,8,9]
print(pairsThatEqualSum(nums1,10)) #[5,5] bug
print(pairsThatEqualSum(nums2,0))
print(pairsThatEqualSum(nums3,1))