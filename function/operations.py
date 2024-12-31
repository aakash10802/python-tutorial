# Write a program that allows a user to:

# Add a number to the list.
# Remove a number from the list.
# Display the maximum number in the list.
# Display the minimum number in the list.
# Calculate the sum of all numbers in the list.
# Display all numbers in the list.
# Exit the program.
# Each operation should be a separate function, and the program should continue until the user chooses to exit.
numbers = []

 
def add_number(num):
    numbers.append(num)
    print(f"{num} added to the list.")

def remove_number(num):
    if num in numbers:
        numbers.remove(num)
        print(f"{num} removed from the list.")
    else:
        print(f"{num} not found in the list.")

def find_max():
    if numbers:
        return max(numbers)
    else:
        return "List is empty."

def find_min():
    if numbers:
        return min(numbers)
    else:
        return "List is empty."

def calculate_sum():
    return sum(numbers)

def display_numbers():
    if numbers:
        print("Current numbers in the list:", numbers)
    else:
        print("List is empty.")

# Main program loop
while True:
    print("\nSelect operation:")
    print("1. Add a number")
    print("2. Remove a number")
    print("3. Display the maximum number")
    print("4. Display the minimum number")
    print("5. Calculate the sum of all numbers")
    print("6. Display all numbers")
    print("7. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        print("Exiting program.")
        break

    if choice == '1':
        num = int(input("Enter a number to add: "))
        add_number(num)
    elif choice == '2':
        num = int(input("Enter a number to remove: "))
        remove_number(num)
    elif choice == '3':
        print("Maximum number in the list:", find_max())
    elif choice == '4':
        print("Minimum number in the list:", find_min())
    elif choice == '5':
        print("Sum of all numbers:", calculate_sum())
    elif choice == '6':
        display_numbers()
    else:
        print("Invalid choice! Please try again.")