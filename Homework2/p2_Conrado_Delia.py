#Problem 2.a List Comprehension function
"""
checklist:
1. tuple: consist of 4
2. every element in tuple is different from each other
3. have to be of range 10
4. a^2 + b^2 = c^2 +d^2"""

#list_comp_no1 = [(a, b, c, d) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11) for d in range(1, 11) if len({a,b,c,d}) == 4 and a^2 +b^2 == c^2 +d^2]
#testing output
#print(list_comp_no1)

#Problem 2.b List Comprehension function
"""
checklist:
1. Tuples: list of strings
2. 1st element: lowercase version from initial
list[0] = lst.lower()
3. 2nd element: len(second_element)
list[1] = lst.len(second_element)
4. strings in list have to be > 5 characters
if len(list[]) <= 5"""

#list created for testing
word_list = ['One', 'two', 'Seven', 'four']
list_comp_no2 = [(word.lower(), len(word)) for word in word_list if len(word) < 5]
#testing output
print(list_comp_no2)

#Problem 2.c list comprehension
"""
Checklist
1. list format: firstname, middlename, lastname
2. list elements: firstname middlename_inital lastname"""

#testing name list
names = ['Brian Matthew Miller', 'Delia Alejandra Conrado']
list_comp_no3 = [(name.split()[0] + " " + name.split()[1][0]+". "+ name.split()[2]) for name in names]

#testing output
print(list_comp_no3)

#Problem 2.d list comprehension
"""
checklist:
1. input: two lists
2. tuple: w1 from list one and w1 from list two
3. 

"""
#lists from assignment to test
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

list_comp_no4 = [(w1, w2) for w1 in lst1 for w2 in lst2 if sorted(w1.lower()) == sorted(w2.lower())]

#testing list function output
print("list_comp_no4")

#Problem 2.e dictionary comprehension
"""
Checklist:
1.dictionary comprehension function
2. first element: string
3. second element: len(str)
"""
#list for testing dictionary function
s = ['one', 'two', 'three']

dict({word:len(word) for word in s})

#testing output from dictionary function
print(dict({word:len(word) for word in s}))

#Problem 2.f dcitionary comprehension
"""
Checklist:
1.dictionary comprehension
2. text = str
3. dict(i:c)
4. i= index of character
5. c: vowels.lower()"""

#testing variable
text = "Hello Universe"

dict({i:c for i,c in enumerate(text) if c in "aeiou" or "AEIOU"})

#testing dictionary function output
print(dict({i:c for i,c in enumerate(text) if c in "aeiouAEIOU"}))

