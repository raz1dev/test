print("Hi")
# Creating an array (list) with some elements
my_array = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_array[0]  # Access the first element
last_element = my_array[-1]  # Access the last element

# Modifying elements
my_array[0] = 10  # Change the first element to 10

# Adding elements
my_array.append(6)  # Add 6 to the end of the array

# Removing elements
my_array.remove(2)  # Remove the element 2 from the array

# Getting the length of the array
array_length = len(my_array)  # Returns the number of elements in the array

# Iterating over the array
for element in my_array:
    print(element)  # Prints each element in the array



def find_shortest_repeating_substring(s):
    # Function to check if the string can be constructed by repeating a substring
    def can_construct_from_substring(substring, s):
        repeats = len(s) // len(substring)
        constructed = substring * repeats
        diff_count = sum(1 for a, b in zip(constructed, s) if a != b)
        return diff_count <= 1

    # Main logic to find the shortest repeating substring
    for i in range(1, len(s) + 1):
        if len(s) % i == 0:
            substring = s[:i]
            if can_construct_from_substring(substring, s):
                return i
    return len(s)

# Example usage:
# Read the number of test cases
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    # Read the length of the string and the string itself
    n = int(input("Enter the length of the string: "))
    s = input("Enter the string: ")
    # Find and print the length of the shortest repeating substring
    print(find_shortest_repeating_substring(s))
