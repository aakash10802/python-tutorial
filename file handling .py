

#1. Read a File and Count Word Occurrences
#Problem:

#Open a file called input.txt.
#Read through the file line by line.
#Count how many times the word "Python" appears in the file

#first method
word_to_count = "Python"
 count = 0
 with open("input2.txt","r")as file :
    for line in file:
        count += line.lower().split().count(word_to_count.lower())
 print(f"The word '{word_to_count}'appears {count} times.")


#Second Method

word = "Python"
count = 0
file= open("input2.txt","r")
for line in file :
    count += line.lower().split().count(word.lower())
print(f"the word  '{word}' is used {count} times")


2. Write Even Numbers to a File
Problem:

Create a new file called even_numbers.txt.
Use a for loop to generate numbers from 1 to 100.
Write only even numbers to the file, each on a new line

with open("even_numbers.txt", "w") as file:
    for number in range(1, 101):
        if number % 2 == 0:
            file.write(f"{number}\n")
