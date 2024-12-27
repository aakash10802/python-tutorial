input_string="beautiful day"
vowels="aeiouAEIOU"
result_string = ''.join([char for char in input_string if char not in vowels])
print(result_string)