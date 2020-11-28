import time
start = time.time()
x = (x*x for x in range(100000))
for i in x:
    print(i)
end = time.time()

start1 = time.time()
x = [x*x for x in range(100000)]
for i in x:
    print(i)
end1 = time.time()

print('generators: ', end - start, '\nlist: ', end1 - start1)
