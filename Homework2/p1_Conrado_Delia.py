#Problem 1.a function creation
def line_number(first_file: str, second_file: str):
    #Docstring for function
    """
    reads the file indicated by the first parameter and writes its
    lines prefixed by the line number to the file represented by the second parameter   
    """

    #Reading the file that is from the first parameter of the function and writing to the file that is from the second parameter
    try:
        input_file = open(first_file, "r")
        output_file = open(second_file, "w")

        #Variable that will hold our line number to apply to line from file
        line_number = 1

        #for loop for applying line number to line comping from file no.1
        for line in input_file:

            #makingn sure we only have one new line when writting back the line to output file
            new_line = line.rstrip("\n")
            print(line_number, new_line, file=output_file)

            #increasing line number by one each iteration of loop to get the apropriate line number for each line
            line_number = line_number + 1

        #Closing file after loop to save work done during loop
        input_file.close()
        output_file.close()

    #Exception for entering an invalid filename
    except FileNotFoundError:
        print("You must provide a valid file name.")
        raise


#Problem 1.b function creation
def parse_function(py_file: str):
    #Docstring for function
        """
        Reads and parses the Python file and returns a tuple of tuples where each tuple
        has its element 0 the line number of the function definition, element 1 the function name, element 2 the
        formal argument list as a string, and element 3 the function code as a string (signature and body), with
        all empty lines and comments removed  
        """

        #Reading the python file that is from the parameter of the function
        try:
            input_file = open(py_file, "r")

            #using variable to store lines of text from file
            text = input_file.read()
            #close file to save
            input_file.close()

            #Separate the file into lines to prase through and count how many lines are in the file
            lines = text.splitlines()
            lines_count = len(lines)
            

            #list variable to store functions as they are found
            functions = []

            #for loop to iterate through the lines of the file
            for i in range(lines_count):

                line = lines[i]

                #Searching for the "def" that determines the start of a function
                if line.startswith("def "):

                    #Removing any comments that are found in the function
                    if "#" in line:
                        line = line.split("#")[0].rstrip()

                    #Extracting function name
                    func_name = line.split("(")[0]
                    func_name = func_name.replace("def ", "")

                    #extracting the parameters from the function
                    parameters = line.split("(")[1]
                    parameters = parameters.split(")")[0]

                    #Start storing the function code
                    func_code = line + "\n"

                    j = i + 1

                    #initiate while look to look into the lines following the function
                    while j < len(lines):

                        #if statement to break look if another function is encountered
                        if lines[j].startswith("def "):
                            break

                        #if statement to break loop if it iterates through the full function
                        if lines[j] != "" and not lines[j].startswith((" ", "\t", "#")):
                            break

                        #if statements to handle encountering empty lines and comments in python file
                        if lines[j].strip() != "" and not lines[j].strip().startswith("#"):
                            func_code = func_code + lines[j] + "\n"

                        j = j + 1

                    #append into list line number, function name, parameters and lines in function
                    functions.append((i + 1, func_name, parameters, func_code))

            #variable to get the length of the function list
            len_function = len(functions)

            #for loop to iterate and sort alphabetically for tuple output
            for i in range(len_function):
                for j in range(i + 1, len_function):

                    if functions[i][1] > functions[j][1]:
                        functions[i], functions[j] = functions[j], functions[i]

            #converting list into tuples and returning results
            return tuple(functions)

        #exception for not finding file that is provided
        except FileNotFoundError:
            print("Error: File not found.")

        #exception to not being able to read file that is provided
        except Exception:
            print("Error reading or parsing file.")
            raise
        
                
def main():

#Two input varibles to the the names of the two files needed for the above function to be called
    first_file_name = input("Please provide the full file(including file extension) you would like to read from: ")
    second_file_name = input("Please provide the full file(including file extension) you would like to write to: ")

#input for getting python file to call function fofr problem 1.b
    py_file = input("Please provide python file you would like to look at: ")

    #testing for problem 1.a
    line_number (first_file_name, second_file_name)

    #testing for problem 1.b
    print(parse_function(py_file))

#calling main function
if __name__ == "__main__":
    main()
    


        
        



        




