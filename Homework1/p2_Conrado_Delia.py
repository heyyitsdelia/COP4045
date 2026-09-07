def find_Pythagorean(n):
#condition to check if number is a positive int, if not, it does not go through the loop
    if n < 0:
        return "not a positive int"

    #list to store values that pass test
    tuples = []

    #starting value for c
    c = 1
    #loop for using n value to find possible combinations
    while c <= n:
        #starting value for b
        b = 1
        
        while b <= n:
            #starting value for 1
            a = 1
            while a <= n:
                #condition for iterating and adding to list
                if a**2 + b**2 == c**2:
                    #function add a b and c to a list
                    tuples.append((a,b,c))

                    
                a = a + 1

            b = b + 1

        c = c + 1
    return tuples


##testing function
n = int(input("please provide an int: "))
print(find_Pythagorean(n))


