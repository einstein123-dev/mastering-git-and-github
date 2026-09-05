#normal traditional for loop

numbers = [1,2,3,4,5,6,7,8,9]

squared_numbers = []
for number in numbers:
    number_squared = number ** 2
    squared_numbers.append(number_squared)

print(squared_numbers)


#using list comprehension

squared_numbers1 = [x **2 for x in range(1,10)]
print(squared_numbers1)

message = f"You are {squared_numbers1[3]} years old in squared numbers."
print(message)

