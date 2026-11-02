##Python Assignment question No.5

import turtle

#problem 5.a-Drawing a recursive leaf
def draw_leaf_straight(level: int, length: float) -> None:
    """
    draw_leaf_straight that draws a leaf-
    like that looks like Figure 1.a) using the turtle module
    """
    # base case when level reaches 0
    if level == 0:
        return

    #drawing the stem
    turtle.forward(length)

    #drawing left branch
    turtle.left(40)
    draw_leaf_straight(level - 1, length * 0.55)
    turtle.right(40)

    # drawing the right branch
    turtle.right(40)
    draw_leaf_straight(level - 1, length * 0.55)
    turtle.left(40)

    # Continue the center stem
    turtle.forward(length * 0.55)
    draw_leaf_straight(level - 1, length * 0.55)

    # Return to the starting position
    turtle.backward(length * 0.55)
    turtle.backward(length)


#problem 5.b - Extra Credit
def draw_leaf_curved(level: int, length: float) -> None:
    """
    Extra credit: 5 points if you also write a similar function called draw_leaf_curved (in addition to
    draw_leaf_straight) that draws a curved leaf that looks like that in Figure 2. Again, it does not have to
    be identical, but the leaf must be curved
    """

    if level == 0:
        return

    # Draw a curved stem
    turtle.circle(-330, length / 6)

    # Save the turtle's position and direction
    position = turtle.pos()
    direction = turtle.heading()

    # Draw the left branch
    turtle.left(40)
    draw_leaf_curved(level - 1, length * 0.55)

    # Return to the branching point
    turtle.up()
    turtle.goto(position)
    turtle.setheading(direction)
    turtle.down()

    # Draw the right branch
    turtle.right(40)
    draw_leaf_curved(level - 1, length * 0.55)

    # Return to the branching point
    turtle.up()
    turtle.goto(position)
    turtle.setheading(direction)
    turtle.down()

    # Continue the center branch
    draw_leaf_curved(level - 1, length * 0.55)

def main():
    turtle.speed(0)
    turtle.delay(0)

    #turtle back to starting position
    turtle.up()
    turtle.goto(0, -250)
    turtle.setheading(90)
    turtle.down()
    #testing the draw_leaf_straight function
    #draw_leaf_straight(6, 120)

    #testing the draw_leaf_curved function
    draw_leaf_curved(6, 120)

    turtle.done()

if __name__ == "__main__":
    main()

#problem 5.b-creating Base X Conversion
def strB(n: int, base: int = 10) -> str:
    """
    Write in file Write a function in file p2_Lastname_Firstname.py a recursive function
    strB(n, base=10) that converts a non-negative int value n to a string representation of n in the given
    base. The base parameter is an int between 2 and 26.
    For digits greater than 9 use letters ‘A’-’Z
    """

    #checking for invalid values
    if n < 0:
        raise ValueError("can't be negative.")

    if base < 2 or base > 26:
        raise ValueError("must be between 2 and 26.")

    #characters used for each digit up to 9, after that letters A-Z are used
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #establishing the base case
    if n < base:
        return digits[n]

    #establishing the recursive case
    return strB(n // base, base) + digits[n % base]

#testing for problem 5.b
#print(strB(100, 16))
#print(strB(123, 16))
#print(strB(16, 2))
#print(strB(15, 25))

#function needed for part b
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b

#problem 5.b-builindg 4 Unit tests
def test_strB() -> None:
    """
    Use the testif module/function attached to the homework’s page to write 4 unit tests for the strB
    function. Check out Homework 3 solutions on how to write these unit tests
    """

    #testinf for converting to base 16
    testif(strB(100, 16) == "64", "Base 16 conversion")

    #testing for converting to base 16
    testif(strB(123, 16) == "7B", "Base 16 conversion")

    #tessting for converting to base 2
    testif(strB(16, 2) == "10000", "Base 2 conversion")

    #testing for converting to base 25
    testif(strB(15, 25) == "F", "Base 25 conversion")

#testing the test_strB function for problem 5.b
test_strB()

#problem 5.c_ creatingBinomial Coefficient function
def Cnk_m(n: int, k: int, memory: dict = None) -> int:
    """
    function Cnk_m(n,k) for computing the value of
    the binomial coefficient using the memoization technique taught in class
    """

    #conditional statement to check for invalid values
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid n and k values")

    #conditional statement to create a dictionary if one does not exist
    if memory is None:
        memory = {}

    #conditional statement to check if the result was already calculated
    if (n, k) in memory:
        return memory[(n, k)]

    #conditional statement to establish Base cases
    if k == 0 or k == n:
        return 1

    #creating recursive case
    result = Cnk_m(n - 1, k - 1, memory) + Cnk_m(n - 1, k, memory)

    # Save the result in the dictionary
    memory[(n, k)] = result

    return result

# Problem 5.c - Unit tests
def test_Cnk_m() -> None:
    """
    Testing Cnk_m function using testif().
    """

    #Test case no. 1
    testif(Cnk_m(5, 2) == 10, "Cnk_m(5, 2)")

    #Test case no.2
    testif(Cnk_m(6, 3) == 20, "Cnk_m(6, 3)")

    #Test case no. 3
    testif(Cnk_m(8, 4) == 70, "Cnk_m(8, 4)")

    #Test case no. 4
    testif(Cnk_m(10, 5) == 252, "Cnk_m(10, 5)")

#testing the Cnk_m function for problem 5.c
#print(Cnk_m(5, 2))
#print(Cnk_m(6, 3))
#print(Cnk_m(8, 4))

#testing the 4 unit test for Cnk_m function for problem 5.c
test_Cnk_m()

#problem 5.d - Making Pairs
def make_pairs(seq1: list, seq2: list, pairs: list = None) -> list:
    """
    called make_pairs that takes as
    parameters two lists, seq1 and seq2, and that returns a list with all tuples (x, y) where x is in seq1 and y
    is the matching element in seq2, at the same index as x.
    Function make_pairs stops once it reaches the end of the shorter sequence.
    """

    #creating an empty accumulator list
    if pairs is None:
        pairs = []

    case_1 = len(seq1)
    case_2 = len(seq2)
    #establishing base case
    if case_1 == 0 or case_2 == 0:
        return pairs

    #append the matching elements to the accumulator list
    pairs.append((seq1[0], seq2[0]))

    #creating and establishing recursive case
    return make_pairs(seq1[1:], seq2[1:], pairs)

#problem 5.d-testing 4 test cases for Making Pairs
def test_make_pairs() -> None:
    """
    Testing the make_pairs function using testif().
    """
    #testing test case no. 1 - Equal length lists
    testif(make_pairs([1, 2, 3], [4, 5, 6]) ==[(1, 4), (2, 5), (3, 6)], "Equal length lists")

    #testing test case no.2 - Second list is shorter
    testif(make_pairs([1, 2, 3], [4, 5]) ==[(1, 4), (2, 5)], "Second list shorter")

    # testing test case no. 3 - First list is shorter
    testif(make_pairs([1, 2], [4, 5, 6]) ==[(1, 4), (2, 5)], "First list shorter")

    # testing test case no. 4 - First list is empty
    testif(make_pairs([], [4, 5, 6]) ==[], "First list empty")

    # testing test case no. 5 - Second list is empty
    testif(make_pairs([1, 2, 3], []) ==[], "Second list empty")

#testing function for the four test cases
test_make_pairs()