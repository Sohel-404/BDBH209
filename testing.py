data = [44,46,49,52,55,62,67,72,77,80,83,86,88,90,92,94,99,100,101,106]

data = [str(i) for i in data]
c = {i: data.count(i) for i in data}
mod = max(c, key=lambda x: c[x])
print(all(x==1 for x in data))

print(mod)