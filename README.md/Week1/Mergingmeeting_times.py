from operator import itemgetter

m=((0, 1), (3, 5), (4, 8), (10, 12), (9, 10))

if len(m) <= 1:
    print("Not possible")

m= sorted(m,key=itemgetter(0))
pdl = [m[0]]
    # print(pdl)
m = m[1:]
for (s1,e1) in m:
    (s,e) = pdl[-1]
        
    if e>=s1:
        if e<=e1:
            e = e1
        pdl[-1] = (s,e)
    else:
        pdl.append((s1,e1))

print(pdl)