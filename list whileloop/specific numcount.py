num = int(input("Enter a number: "))
digit_to_count = int(input("Enter the digit to count: "))
count = 0
while num > 0:
    if num % 10 == digit_to_count:
        count += 1
    num //= 10
print(f"The digit {digit_to_count} appears {count} times.")
