def extra_candy
a=[2,3,5,1,3]
max=a[0]
extra=3
op = []
for i in range(len(a)):
    if(max<a[i]):
        max=a[i]
for i in a:
    if(max < a + extra):
        op.append("true")
    else:
        op.append("false")
return op

