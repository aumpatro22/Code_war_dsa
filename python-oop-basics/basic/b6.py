arr = [5, 3, 8, 1]

# Access
print(arr[0])  # 5

# Update
arr[3] = 10

# Traverse
for x in arr:
    print(x)

# Search
if 8 in arr:
    print("found at", arr.index(8))

# Insert
arr.append(12)          # add at end
arr.insert(2, 7)        # add in middle

# Delete
arr.pop(1)
arr.remove(10)

# Sort
arr.sort()
print(arr)