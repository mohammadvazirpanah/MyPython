scores = [ ["Joe",20,10,12,8.565454] , ["Damon",20,20.46454,19.546545,18.5] ,
 ["Jack",20,20,20,20] , ["Nicolas",20,20,20,20] ]

print (scores)

for person in scores : 
    print (person)


for person in scores : 
    for item in person:
        print (item, "|",end = " ")
    print ()
a = 10
b = 230
c = 30.0125452
d = 40 
e = 50 
f = 60 
h = 'mohammad'
my_str = "x = {1} and y = {0} and z = {2}".format (a,b,c,d,e,f)
my_str = "x = {} and y = {}".format (10,20,30,40,50,60)
my_str = "x = {} and y = {}".format (7,13,10,100)
 
my_str = "x ={0:4d} and y ={1:6d} and z ={2:10.4f} and my name is {6:10s} and Table is:".format (a,b,c,d,e,f,h)
print (my_str)


for person in scores : 
    for item in person:
        if type (item) ==str:
            print ("{0:20s} | ".format(item), end ="")
        else: 
            print ("{0:^10.0f} |".format(item),end="")
    print ()

str = " str is _{0:x<10d}_".format(100)
print (str)

str1 = " str is _{0: ^10d}_".format(100)

print (str1)




def reverse_str (s):
    r = ""
    for char in s:
        r = char + r
    return r 

def reverse_str_2 (s):
    r = ""
    for i in range (len(s)-1,-1,-1):
        r = r + s[i]
    return r
        

input_str = input ("give me a String: \n")

reverse_1 = reverse_str (input_str)
print (reverse_1)

reverse_2 = reverse_str_2 (input_str)
print (reverse_2)



