list = [30,85,23,17,72,99,44,51,31]
print("")
print("")
print ("Original")
print(list)
print("")

def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for i in range(i):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

bubbleSort(list)

print ("Sorted")
print(list)
print("")
print("")
