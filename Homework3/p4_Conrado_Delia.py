##Python Assignment question No.4

from fileinput import filename

#problem 4.a-creating ed_read function part 1
def ed_read(filename: str, from_: int = 0, to_: int = -1) -> str:
    """
    returns as a string the content of the file named filename,
    with file positions in the half-open range [from_, to_). If to_ == -1, the content between from_ and
    the end of the file will be returned. If parameter to_ exceeds the file length, then the function
    raises exception IndexError with a corresponding error message
    """
    #opening file to read the content and storing it in a variable
    input_f = open(filename, "r", encoding="utf-8")
    text = input_f.read()
    input_f.close()
    #condition statements to check if the start and end positions are valid
    if from_ < 0 or to_ < -1 or (to_ != -1 and to_ < from_):
        raise IndexError("Invalid file positions.")
    #condition statement to check if the start and end positions exceed the file length
    if from_ > len(text) or to_ > len(text):
        raise IndexError("Position exceeds file length.")
    #condition statement to check if the end position is -1
    if to_ == -1:
        return text[from_:]

    return text[from_:to_]
#problem 4.a-creating ed_find function part 2
def ed_find(filename: str, search_str: str) -> list[int]:
    """
    finds string search_str in the file named by filename and returns
    a list with index positions in the file text where the string search_str is located. E.g. it returns
    [4, 100] if the string was found at positions 4 and 100. It returns [] if the string was not found
    """
    #opening file to read the content and storing it in a variable
    input_f = open(filename, "r", encoding="utf-8")
    text = input_f.read()
    input_f.close()
    #list with index positions in the file text
    positions = []

    text_length = len(text)
    for i in range(text_length):
        if text[i:i + len(search_str)] == search_str:
            positions.append(i)

    return positions
#problem 4.a-creating ed_replace function part 3
def ed_replace(filename: str, search_str: str, replace_with: str, occurrence: int = -1) -> int:
    """
    replaces search_str in the file
    named by filename with string replace_with. If occurrence==-1, then it replaces ALL
    occurrences. If occurrence>=0, then it replaces only the occurrence with index occurrence,
    where 0 means the first, 1 means the second, etc. If the occurrence argument exceeds the actual
    occurrence index in the file of that string, the function does not do the replacement. The
    function returns the number of times the string was replaced
    """
    #check for invalid strings and occurqrence
    if search_str == "":
        raise ValueError("Search string cannot be empty.")

    if occurrence < -1:
        raise ValueError("Invalid occurrence number.")
    #opening file to read and store content
    input_f = open(filename, "r", encoding="utf-8")
    words = input_f.read()
    input_f.close()

    #conditional statement to replace all occurrences
    if occurrence == -1:
        new_t = words.replace(search_str, replace_with)
        count = words.count(search_str)

    #Conditional statement to replace a specific occurrence
    else:
        positions = []
        start = 0
        while True:
            position = words.find(search_str, start)
            if position == -1:
                break
            positions.append(position)
            start = position + len(search_str)
        if occurrence >= len(positions):
            return 0
        position = positions[occurrence]
        new_t = words[:position] + replace_with + words[position + len(search_str):]
        count = 1
    #writing the new content to the file
    output_f = open(filename, "w", encoding="utf-8")
    output_f.write(new_t)
    output_f.close()

    return count
#problem 4.a-creating ed_append function part 4
def ed_append(filename: str, string: str) -> int:
    """
    appends string to the end of the file. If the file does not exist, a
    new file is created with the given file name. The function returns the number of characters
    written to the file.
    """

    #opening file in append mode to write string to file
    output_f = open(filename, "a", encoding="utf-8")
    output_f.write(string)
    #closing file to save changes
    output_f.close()
    #counting the number of characters written to the file
    num_chars = len(string)
    return num_chars

# testif module 
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

#problem 4.b-creating test_ed_find function part 1
def test_ed_find() -> None:
    """
    Write test functions for functions ed_replace and ed_find using the testif() function we used for
    homework 3, listed in Appendix A. These test functions should be named test_x , where x is the name
    of the function tested. E.g. test_ed_write() should use testif() to test ed_write(). In general, this type of
    test functions are called unit tests as they test just one function (or one method in a class)
    """
    #test file
    file_name = "dummy_file.txt"

    # Create a test file
    output_f = open(file_name, "w", encoding="utf-8")
    output_f.write("847291628472916352")
    output_f.close()

    #testing for finding two occurrences
    result = ed_find(file_name, "729")
    testif(result == [2, 10], "Find two occurrences")

    #testing when string is not found/does not exist in the file
    result = ed_find(file_name, "555")
    testif(result == [], "Find no occurrences")

    #testing for finding a string at the beginning
    result = ed_find(file_name, "847")
    testif(result == [0, 8], "Find at beginning")

#problem 4.b-creating test_ed_replace function part 2
def test_ed_replace() -> None:
    """
    Write test functions for functions ed_replace and ed_find using the testif() function we used for
    homework 3, listed in Appendix A. These test functions should be named test_x , where x is the name
    of the function tested. E.g. test_ed_write() should use testif() to test ed_write(). In general, this type of
    test functions are called unit tests as they test just one function (or one method in a class)
    """
    #test file
    file_name = "dummy_replace.txt"

    #writing to the file to test replacing all occurrences
    output_f = open(file_name, "w", encoding="utf-8")
    output_f.write("847291628472916352")
    output_f.close()

    #testing for replacing all occurrences
    result = ed_replace(file_name, "729", "abc")
    words = ed_read(file_name)
    testif(result == 2 and words == "84abc16284abc16352","Replace occurrences")

    #resetting file
    output_f = open(file_name, "w", encoding="utf-8")
    output_f.write("847291628472916352")
    output_f.close()

    #testing for replacing only the second occurrence
    result = ed_replace(file_name, "729", "qrs", 1)
    words = ed_read(file_name)
    testif(result == 1 and words == "8472916284qrs16352", "Replace second occurrence")

    #testing for replacing a string that does not exist
    result = ed_replace(file_name, "626", "ABC")
    testif(result == 0, "Replace no occurrences")

def main() -> None:
    """
    Write a main() function where you show how to use all ed_…. functions written for part a).
    """

    file_name = "dummy_file.txt"
    #dummy test file to test the functions
    output_f = open(file_name, "w", encoding="utf-8")
    output_f.write("7862523539")
    output_f.close()

    #testing ed_append
    print("ed_append test:")
    result = ed_append(file_name, "7862523539")
    print("Appended:", result)

    #testing ed_read
    print("\ned_read test:")
    print("text:", ed_read(file_name, 3, 9))
    print("position 3:", ed_read(file_name, 3))

    #testing ed_find
    print("\ned_find test:")
    print("found:", ed_find(file_name, "252"))
    print("not found:", ed_find(file_name, "999"))

    #testing ed_replace
    print("\ned_replace test:")
    result = ed_replace(file_name, "252", "ABC", 1)
    print("# of replacements:", result)
    print("Updated file:", ed_read(file_name))

    #testing funtions
    test_ed_find()
    test_ed_replace()


#test main function
if __name__ == "__main__":
    main()

