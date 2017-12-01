#!/usr/bin/python

import random
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Lock, Array
import matplotlib.pyplot as plt

def createList(size):
    list = []
    for i in range(0,size):
        list.append(random.randint(0, 39))
    return list

def createHistogram(size):
    list = [0]*40
    return list

def hist(list, histogram, lk):
    for l in list:
        histogram[l] = histogram[l] + 1
    return histogram
    
l = Lock()
pool = Pool(processes=2)

list = createList(100)
histogram = createHistogram(40)
hist(list,histogram,l)
arr = Array('i', range(40))
for k in range(0,40):
    arr[k] = 0

p1 = Process(target=hist, args=(list[0:25], arr, l))
p2 = Process(target=hist, args=(list[25:50], arr, l))
p3 = Process(target=hist, args=(list[50:75], arr, l))
p4 = Process(target=hist, args=(list[75:100], arr, l))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

out_list_1 = createList(40);
out_list_2 = createList(40);
out_list_3 = createList(40);

for i in range(0,40):
    out_list_1[i] = (arr[i] - histogram[i])
    out_list_2[i] = arr[i];
    out_list_3[i] = i;

print("Index:")
print(out_list_3);
print("Histogram funkcja:")
print(histogram);
print("Histogram watkami:")
print(out_list_2);
print("Roznica miedzy dwoma metodami:")
print(out_list_1);

plt.hist(list, bins = 40)
plt.show();