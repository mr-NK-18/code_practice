def isValid(s):

    store = []

    check = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for i in s:

        if i in check.values():
            store.append(i)

        elif i in check.keys():

            if not store:
                return False

            if store.pop() != check[i]:
                return False

    return store == []

# Driver Code
s = input("Enter brackets: ") #{)[}

print(isValid(s))