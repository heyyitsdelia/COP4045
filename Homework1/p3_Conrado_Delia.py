import pandas as pd

#function for question 3 part a
def find_dup_str(s,n):
    #variables for loop
    i=0

    #check if substring is longer than string, if longer, doesnt run through loop
    if n > len(s):
        return -1
    #checks if substring is equal to or greater than 4, if so returns ""
    if n >= 4:
        return ""
    
    #iterates through to find substring
    while i < len(s)-n:

        #slicing used to go through the string to find substring
        ss = s[i:i+n]
        j = i +1

        #slicing through string again to find duplicates
        while j < len(s)-n:
            ss_duplicate = s[j:j+n]
            if ss == ss_duplicate:
                return ss
            #increment for inner while loop
            j = j + 1
        #increment for outer while loop
        i = i + 1

    return ""       
    
s = input("Please provide a string: ")
n = int(input("Please provide a substring length to search for: "))

print(find_dup_str(s,n))

#testing variables
#print (s,n)
#print(len(s))
#print(n)
    
#function for question 3 part b
def find_max_dup(s):
    #variable to store longest substring and n starting substring length off at 1
    longest_dup_ss = ""
    n = 1

    #for loop for iterating through string using its length while also calling function from question 3a
    for n in range(1, len(s) + 1):
        #function call for function from part a
        ss = find_dup_str(s,n)

        #Checking if result is "", "" means there is no substring
        if ss != "":
            #substring found, if ss is longer, longer becomes that substring
            longest_dup_ss = ss
            #print(longest)

    return longest_dup_ss

#Testing
s = input("Please provide a string: ")
print(find_max_dup(s))



