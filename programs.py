def factorial(n):
    if n == 0:
        return 1
    else:
        return n  * factorial(n-1)
num = int(input("Enter a Number:"))
print(factorial(num))

def is_prime(num):
    for i range(2,num):
        if num % in !=0:
        return True
    return False
num = int(input)("Enter the string :"))
print(is_prime)

str = input("Enter a string : ")
if str==str[::-1]:
    print(str, "is palindrome")
else:
    print(str, "not palindrome")

    def sum_of_digits(number):
        return sum(int(digit)for digit in str (abs(number)))
    num = int(input("enter a number: "))
    print(sum_of_digits)

    def fibonacci_series(n):
        fib_series = [0,1]
        while = fib_series
num = int (input("Enter the limit for fibpnacci series : "))
print(fibonacci_series)

def largest_number(input_str):
    largest_number= max(mylist)
    return largest_number
mylist=[23,121212,34,55,899]
print(largest_number(mylist))

def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str
input_string = input("Enter a string: ")
result = reverse_string(input_string)
print(f"The reversed string is: {result}")

def find_intersection(list1, list2):
    return list(set(list1) & set(list2))
list1 = [int(x) for x in input("Enter elements of the first list separated by space: ").split()]
list2 = [int(x) for x in input("Enter elements of the second list separated by space: ").split()]
result = find_intersection(list1, list2)
print(f"The intersection of the two lists is: {result}")

def remove_duplicates(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
numbers = [int(x) for x in input("Enter elements of the list separated by space: ").split()]
result = remove_duplicates(numbers)
print(f"The list after removing duplicates is: {result}")

def rotate_list_to_right(lst, k):
    n = len(lst)
    k = k % n 
    rotated_list = lst[-k:] + lst[:-k]
    return rotated_list
original_list = [1, 2, 3, 4, 5]
k_steps = 2
result = rotate_list_to_right(original_list, k_steps)
print(result)

def second_largest_element(lst):
    if len(lst) < 2:
        return 
    max_element = max(lst)
    lst.remove(max_element)
    second_largest = max(lst)
    return second_largest
input_list = [5, 2, 8, 10, 7]
result = second_largest_element(input_list)
print("Second largest element:", result)

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
sorted_list1 = [1, 3, 5, 7, 9]
sorted_list2 = [2, 4, 6, 8, 10]
result = merge_sorted_lists(sorted_list1, sorted_list2)
print("Merged sorted list:", result)