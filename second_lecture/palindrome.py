# wap to check palindrome or not
# string = input("enter the string:")
# reversed_string = string[::-1]
# print("the reversed string is:", reversed_string)
# if(string == reversed_string):
#     print("the string is palindrome")
# else:
#     print("the string is not palindrome")

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

# Create a copy
new_list = list1.copy()

# Reverse the copied list
new_list.reverse()

print("Original List:", list1)
print("Reversed List:", new_list)

if list2 == new_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")