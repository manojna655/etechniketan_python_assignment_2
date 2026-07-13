s1 = input("Enter a string: ")

count = {}

for ch in s1:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)
