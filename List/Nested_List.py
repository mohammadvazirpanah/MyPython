


def function1():
    list1 = []
    list2 = []
    list3 = []
    count1 = 3
    k=0
    for I1 in range(count1):
        for I2 in range(count1):
            for I3 in range(count1):
                list3.append(k)
                k=k+1
            list2.append(list3)
            list3 =[]
        list1.append(list2)
        list2 = []
    return list1

print (function1())

list = function1()
print (list [2][0][0])



print (list [1][1][2])

