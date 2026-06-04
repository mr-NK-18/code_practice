def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def palindrome(s):
    rev = ""
    for ch in s:
        rev = ch + rev

    if s == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"

while True:
    print("\n1. Reverse String")
    print("2. Check Palindrome")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        s = input("Enter string: ")
        print(reverse_string(s))

    elif choice == 2:
        s = input("Enter string: ")
        print(palindrome(s))

    elif choice == 3:
        break

    else:
        print("Invalid Choice")
