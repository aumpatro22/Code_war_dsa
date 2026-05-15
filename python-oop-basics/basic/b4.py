number = [1,2,3,4,5,6,7]
sum_val = 0   # avoid naming it 'sum' (conflicts with built-in)

for i in range(len(number)+1):
    if i == 0:
        print("The first element in the list:", number[i])
    elif i == len(number):
        print("The last element in the list:", number[-1])

# middle element
mid_index = len(number) // 2
print("The middle element in the list is:", number[mid_index])

# average (mean)
print("The average of the list is:", int(sum(number)/len(number)))

number.append(98)
number.remove(1)
for i in range(len(number)):
    print(number[i])

print("the largets in the list is")
largest=number[0]
for i in range(1,len(number)):
    if number[i] >largest:
        largest=number[i]
     
print("The largest element in the list is:", largest)


