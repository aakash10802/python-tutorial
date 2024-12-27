words = ["level", "world", "radar", "python", "madam", "hello"]

palindromes = [word for word in words if word == word[::-1]]

print(palindromes)

# ::-1 is a slicing technique that reverses the string. If the reversed string is equal to the original string, then it is a palindrome.