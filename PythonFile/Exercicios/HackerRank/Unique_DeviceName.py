from collections import Counter

uniqueDevicename = []
list = []
n = int(input())


for i in range(0, n):
    devicename = str(input())
    list.append(devicename)
    qtd = Counter(list)
    x = qtd[devicename]
    if devicename in uniqueDevicename:
        uniqueDevicename.append(devicename + str(x-1))
    else:
        uniqueDevicename.append(devicename)

for j in range(len(uniqueDevicename)):
    print(uniqueDevicename[j])
