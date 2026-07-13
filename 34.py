words = ["aba", "abc", "1991", "wow", "python", "madam", "hi"]

count = 0

for word in words:
    if len(word) > 2 and word == word[::-1]:
        count += 1

print("Number of palindromes:", count)
