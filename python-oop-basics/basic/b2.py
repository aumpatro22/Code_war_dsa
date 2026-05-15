# Check even or odd
# Check positive, negative, or zero
# Find larger between 2 numbers
# Take marks input:
# above 90 → A
# above 70 → B
# else → C
store=int(input("Enter an number to check it is evene and odd"))
if store%2==0:
    print("even")
else:
    print("not even")
print("checking whether the number is postive,negative or zero")
if store > 0:
    print("positive number")
elif store<0:
    print("negative number")   
else:
    print("zero")

print("grade of student")
marks=int(input("Enter the marks of student"))
if marks >90:
    print("A")
elif marks >80:
    print("A-")
elif marks>70:
    print("B")
else:
    print("c")