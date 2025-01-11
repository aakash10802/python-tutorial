# def show(words):
#     k = []  
#     vowels = ["a", "e", "i", "o", "u"]

#     for word in words:
#         for char in word:
#             if char in vowels:
#                 k.append(word)
#                 break 
#     print(k)
# a = ["fly", "apple", "sky", "education", "spy", "kite", "rhythm", 'rain']
# show(a)
# Write a function extract_words_with_letter(words, letter) that takes a list of words and a specific letter. 
# It should return a list of words that contain that letter at least once.

# def extract_words_with_letter(words, letter):
#     result = []
#     for word in words:
#         if letter in word:
#             result.append(word)
#     return result
# words = ["banana", "apple", "grape", "mango", "kiwi"]
# print(extract_words_with_letter(words, "a"))


# Write a function words_starting_with_vowel(words) 
# that takes a list of words and returns a list of words that start with a vowel.

# def words_starting_with_vowel(words):
#     vowels = "aeiou"
#     result = []
#     for word in words:
#         if word[0].lower() in vowels:
#             result.append(word)
#     return result

# words = ["apple", "banana", "orange", "umbrella", "grape", "elephant"]
# print(words_starting_with_vowel(words))



# Write a function count_vowels_in_words(words) that takes a list of words and returns a dictionary 
# where each word is a key, and its value is the number of vowels in that word.

# def count_vowels_in_words(words):
#     vowels = "aeiou"
#     result = {}
#     for word in words:
#         count = 0
#         for char in word:
#             if char in vowels:
#                 count += 1
#         result[word] = count
#     return result

# words = ["apple", "banana", "grape"]
# print(count_vowels_in_words(words))


# Write a function filter_words_by_length(words, length) that takes a list of words and an integer length. 
# It should return a list of words with length greater than or equal to the specified length.


# def filter_words_by_length(words, length):
#     result = []
#     for word in words:
#         if len(word) >= length:
#             result.append(word)
#     return result

# words = ["apple", "banana", "grape", "kiwi"]
# print(filter_words_by_length(words, 5))

# Write a function separate_even_odd_length_words(words) that takes a list of words and 
# returns two lists: one containing words with an even length and another with words with an odd length.

# def separate_even_odd_length_words(words):
#     even_length_words = []
#     odd_length_words = []
#     for word in words:
#         if len(word) % 2 == 0:
#             even_length_words.append(word)
#         else:
#             odd_length_words.append(word)
#     return even_length_words, odd_length_words

# words = ["apple", "banana", "grape", "kiwi", "pear"]
# print(separate_even_odd_length_words(words))



def evens(words):
    even=[]
    odd=[]
    for word in words:
        if len(word)%2 ==0:
            even.append(word)
        else:
            odd.append(words)
    return even,odd

words=[]