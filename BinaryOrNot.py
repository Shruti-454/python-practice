s = input("Enter a number:")

# check if all characters are '0' or '1'
for char in s:
    if char not in '01':
        print("No, not a binary number")
        break
else:
    print("Yes, it is a binary number")