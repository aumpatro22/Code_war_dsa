# # Print all even numbers from 1 to 100
# for i in range(1,100+1):
#     if i%2:
#         print(i)
# Find sum from 1 to n
# Example:
# n = 5
# output:
# 1+2+3+4+5 = 15
# n=13
# sum=0
# for i in range(1,n):
#     sum=sum+n   
# print(sum)  
# Example:
# "Aum" → "muA"

# Check palindrome

# Example:
# "madam" → palindrome
# "aum" → not palindrome
name = input("Enter any name to reverse and check whether it is reversed or not ")
rev = name[::-1]
print(rev)
if name == rev:
    print("It's a palindrome")
else:
    print("It is not a palindrome")