#This program uses recursion to perform multiple different functions

"""
This function accepts a string as its parameter and replaces all
adjacent letters in the string with only one of that letter it then
returns this new string
"""
def collapse_string(aString):
    if len(aString) <= 1:
        return aString
    if aString[0] == aString[1]:
        return collapse_string(aString[1:])
    else:
        return aString[0] + collapse_string(aString[1:])

"""
This function accepts a positive integer as its perameter and prints a
sequence of numbers generated from n by the following rules:
1. if n is 1, the sequence ends
2. if n is even, divide n by 2 to get the next number in the sequence
3. if n is odd, multiply n by 3 and add 1 to get the next number in the sequence.
"""
def hailstone(n):
    print(int(n), end = ",")
    if n == 1:
        return
    elif n % 2 == 0:
        return hailstone(n/2)
    else:
        return hailstone(n * 3 + 1)

"""
This function searches a list of integers to determine whether there are three
numbers in the list that sum to a certain value. If there exist three integers
that sum to that value, the function will return True. Otherwise, it will
return False.
The parameters are: a list of integers, the length of the list, the desired sum,
and the count - the default which is 0
The three numbers do not need to be consecutive.
"""
def findThree(lis, sum, count = 0):
    listLen = len(lis)
    if listLen <= 2:
        return False
    if lis[count] + lis[count + 1] + lis[count + 2] == sum:
        return True
    else:
        lis.remove(lis[count + 2])
        return findThree(lis, listLen, sum, count + 1)
    
"""
This function accepts two strings as its parameters and returns True if the
two strings are a reverse of each other and False otherwise.
This function ignores capitalization and returns True for the empty string,
as well as strings containing only one letter.
"""
def isReverse(string1, string2):
    if len(string1) == len(string2):
        if len(string1) < 1:
            return True
        if string1[0].lower() == string2[-1].lower():
            return isReverse(string1[1:], string2[:-1])
        else:
            return False
    else:
        return False

"""
This a recusive function that calculates and returns the product of two numbers.
Its parameters are the two numbers
"""
def multiplyNums(firstVal, secondVal):
    if firstVal == 0 or secondVal == 0:
        return 0
    if secondVal == 1:
        return firstVal
    else:
        return firstVal + multiplyNums(firstVal, secondVal -1)

"""
This function accepts a list containing either integers or nested lists,
as well as a target value as its parameters. It returns a count of the number
of times that the target value occurs in the list.
"""
def searchVal(aList, target):
    if len(aList) == 0:
        return 0
    if type(aList[0]) == list:
        return searchVal(aList[0], target) + searchVal(aList[1:], target)
    if aList[0] == target:
        return 1 + searchVal(aList[1:], target)
    else:
        return searchVal(aList[1:], target)

#testing testing
def main():
    print("collapse_string")
    print(collapse_string("sccchoolll"), "Should print schol")
    print(collapse_string("scl"), "Should print scl")
    print(collapse_string(""), "Should print ''")

    print()
    print("hailstone")
    hailstone(7)
    print()
    print("Should print 7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1,")

    print()
    print("findThree")
    print(findThree([2,3],4), "Should return False")
    print(findThree([],4), "Should return False")
    print(findThree([2,3,4],9), "Should return True")

    print()
    print("isReverse")
    print(isReverse("hello", "oLleH"), "Should print True")
    print(isReverse("hellooo", "oLleH"), "Should print False")
    print(isReverse("hellp", "oLleH"), "Should print False")
    print(isReverse("", ""), "Should print True")
    print(isReverse("h", "H"), "Should print True")

    print()
    print("multiplyNums")
    print(multiplyNums(10, 2), "Should print 20")
    print(multiplyNums(10, 0), "Should print 0")
    print(multiplyNums(0, 2), "Should print 0")
    
    print()
    print("searchVal")
    print(searchVal([[2,3],[5,6,7,8],6,[6,7]],6), "Should print 3")
    print(searchVal([[2,3],5,[5,6,5,7,8],6,[6,5,7]],5), "Should print 4")
    print(searchVal([[2,3],5,[5,3,6,5,7,8],6,3,[6,5,3,7],3],3), "Should print 5")
main()
