import readfile 

StringFile = str (readfile.read_func())
print (StringFile)

counter = dict()
#counter = {}   # {"key":value, "h":4, "m":10, .....} 

for letter in StringFile:
	if letter in counter:
		counter[letter] +=1
	else:
		counter[letter] =1  # couter = {"letter":1} -> {"h":1}
        
print (counter)

for i in list (counter.keys()):
	print("%s showed %s times" %(i,counter[i]))





