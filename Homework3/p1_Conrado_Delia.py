##Python Assignment question No.1

class NVector:
    """
    a) constructor. If it has only one argument (besides self) assume it is a sequence of numbers (e.g. a tuple
    or list) and initialize the elements from the NVector accordingly, in a new list object.
    """
    #Problem 1.a and b-Building Constructors
    def __init__(self, *numbers: object) -> None:
        #single arguemtn case
        if len(numbers) == 1:
            self.elements = list(numbers[0])
        #mutilple argument case
        else:
            self.elements = list(numbers)

    #Problem 1.c-Length of vector
    def __len__(self) -> int:
        """
        c) method __len__ that returns the length of the vector. E.g. NVector([3,0,1, -1]).__len_() returns 4.
        Note: x.__len__() is actually invoked when we call len(x)
        """
        return len(self.elements)

    #Problem 1.d-Access an element using its index
    def __getitem__(self, index: int) -> float:
        """
        d) the “index operator” [i], with method __getitem__(index). The argument is an index (an int) into the
        objects element list.
        """
        return self.elements[index]

    #Problem 1.e-Change an element using its index
    def __setitem__(self, index: int, value: int | float) -> None:
        """
        e) the indexed assignment operator [], with method __setitem__(index, value), that will assign value to
        the element at position index
        """
        self.elements[index] = value

    #Problem 1.f-String representation of the vector
    def __str__(self) -> str:
        """
        f) __str__ method that returns the string representation of the NVector object. Pick an obvious format.
        """
        return str(self.elements)

    #Problem 1.g-Check if two vectors are equal (part 1)
    def __eq__(self, other: object) -> bool:
        """
        g) methods __eq__ and __ne__ that take a parameter and return true if self is equal (respectively, not
        equal) to the parameter object, and false otherwise. For __eq__ to return true, self must be compared to
        another NVector object and corresponding elements with the same index should be equal.
        """
        if isinstance(other, NVector):
            return self.elements == other.elements

        return False

    #Problem 1.g-Check if two vectors are different (part 2)
    def __ne__(self, other: object) -> bool:
        """
        Returns True if the vectors are not equal.
        """
        return not self.__eq__(other)

    #Problem 1.h-Adding (part 1)
    def __add__(self, other: object) -> "NVector":
        """
        h) method __add__ for addition with another NVector (done element-wise) or with a number (applied
        to all elements)
        """
        #list to store results
        result = []

        #instance for checking if its another vector we are adding. if so do the lenghts match
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same length.")

            for i in range(len(self)):
                result.append(self.elements[i] + other.elements[i])
        
        #adding number to elements in vector
        elif isinstance(other, (int, float)):
            for i in range(len(self)):
                result.append(self.elements[i] + other)

        else:
            raise TypeError("Can only add an NVector or a number.")

        return NVector(result)

    #Problem 1.h - "Reflected" addition (part 2)
    def __radd__(self, other: object) -> "NVector":
        """
        method __radd__ implementing “reflected” addition, as described in the book.
        """
        return self.__add__(other)

    #Problem 1.i-multiplying (part 1)
    def __mul__(self, other: object) -> int | float:
        """
        methods __mul__ and __rmul__, for scalar multiplication with another NVector or a number and
        “reflected” multiplication.
        """
        #starting point is zero
        result = 0
        #instance for checking if its another vector we are mulitplying. if so do the lenghts match
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same length.")

            for i in range(len(self)):
                result += self.elements[i] * other.elements[i]
        #multiplting numbers to vector check
        elif isinstance(other, (int, float)):
            for i in range(len(self)):
                result += self.elements[i] * other

        else:
            raise TypeError("Can only multiply an NVector or a number.")

        return result

    #Problem 1.i-"Reflected" multiplication (part 2)
    def __rmul__(self, other: object) -> int | float:
        """
        method __rmul__, for scalar multiplication with another NVector or a number and
        “reflected” multiplication.
        """
        return self.__mul__(other)

    #Problem 1.j-Create a vector of zeros
    @classmethod
    def zeros(cls, n: int) -> "NVector":
        """
        j) class method zeros(n) that returns a new NVector object with dimension n with all elements 0.
        """
        if n < 0:
            raise ValueError("cannot be negative.")

        return cls([0] * n)

    #testif module for main function testing
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

#Problem 1.i-testing using testif function
def main() -> None:
    """
    Write a main function that uses the testif() function from Homework 3 (also posted on the
    homework 4’s page and in the Appendix) to test the code from parts a) – i).
    """
    #testing for part a
    nv1 = NVector([5, 3, 7, -1])
    nv2 = NVector((5, 3, 7, -1))

    testif(nv1 == nv2, "__init__", "init works", "init failed")

    #testing for part b
    nv3 = NVector(6, 5, 4, -2)

    testif(nv3.elements == [6, 5, 4, -2], "__init__", "init works", "init failed")

    #testing fot part c
    testif(len(nv1) == 4, "__len__", "len works", "len failed")

    #tesing for part d
    testif(nv1[1] == 3, "__getitem__", "getitem works", "getitem failed")
    testif(nv1[-2] == 7, "__getitem__", "getitem works", "getitem failed")

    #testing for part e
    nv3[2] = 5
    testif(nv3[2] == 5, "__setitem__", "setitem works", "setitem failed")

    #testing for part f
    testif(str(nv1) == "[5, 3, 7, -1]", "__str__", "str works", "str failed")

    #testing for part g
    testif(nv1 == nv2, "__eq__", "eq works", "eq failed")
    testif(nv1 != nv3, "__ne__", "ne works", "ne failed")

    #testing for part h
    nv4 = NVector(7,8,6,2)

    testif(nv1 + nv4 == NVector(12, 11, 13, 1),"__add__", "add works", "add failed")

    testif(nv1 + 10 == NVector(15, 13, 17, 9),"__add__", "add works", "add failed")

    testif(10 + nv1 == NVector(15, 13, 17, 9),"__radd__", "radd works", "radd failed")

    #testing part i
    nv5 = NVector(2, 4, 3, 6)

    testif(nv1 * nv5 == 37, "__mul__", "mul works", "mul failed")

    testif(nv1 * 5 == 70, "__mul__", "mul works", "mul failed")

    testif(5 * nv1 == 70, "__rmul__", "rmul works", "rmul failed")

    #testing part j
    testif(NVector.zeros(4) == NVector(0, 0, 0, 0), "zeros", "zeros works", "zeros failed")

    #testing Exception-when index is invalid
    try:
        nv1[10]
        testif(False, "__getitem__", "getitem works", "getitem failed")
    except IndexError:
        testif(True, "__getitem__", "getitem works", "getitem failed")

    #testing Exception-when assignment index is invalid
    try:
        nv1[10] = 5
        testif(False, "__setitem__", "setitem works", "setitem failed")
    except IndexError:
        testif(True, "__setitem__", "setitem works", "setitem failed")

    #testing Exception -when Addition occurs with different lengths
    try:
        nv1 + NVector(1, 2)
        testif(False, "__add__", "add works", "add failed")
    except ValueError:
        testif(True, "__add__", "add works", "add failed")

    #testing Exception -when Multiplication occurs with different lengths
    try:
        nv1 * NVector(1, 2)
        testif(False, "__mul__", "mul works", "mul failed")
    except ValueError:
        testif(True, "__mul__", "mul works", "mul failed")

    #testing Exception-when constructor agruments are invalid
    try:
        NVector(5)
        testif(False, "__init__", "init works", "init failed")
    except TypeError:
        testif(True, "__init__", "init works", "init failed")

    #testing Exception- when there are Negative dimension
    try:
        NVector.zeros(-3)
        testif(False, "zeros", "zeros works", "zeros failed")
    except ValueError:
        testif(True, "zeros", "zeros works", "zeros failed")

if __name__ == "__main__":
    main()

    

#testing output
#test1 = NVector([3, 0, 1, -1])
#test2 = NVector([1,4,7])
#test2[2] = 5

#print(test1.elements)
#print(test2.elements)
#print(len(test1))
#print(test1[1])
#print(test2.elements)
#print(test2)

#t1 = NVector(3, 0, 1)
#t2 = NVector(3, 0, 1)
#t3 = NVector(5, 2, 1)

#print(t1 == t2)
#print(t1 == t3)
#print(t1 != t3)

#t1 = NVector(3, 0, 1, -1)
#t2 = NVector(1, 2, 3, 4)

#print(t1 + t2)
#print(t1 + 10)
#print(10 + t1)