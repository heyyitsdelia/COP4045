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
