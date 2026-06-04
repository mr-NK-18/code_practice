s="&12#A2sS"

chars=list(s)
print(chars)

for i in range(len(chars)):
    for j in range(i+1, len(chars)):
        if chars[i]>chars[j]:
            temp = chars[i]
            chars[i] = chars[j]
            chars[j] = temp

output=""

for i in chars:
    output += i

print(output)
