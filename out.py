from collections import defaultdict

file = open("out.html")
count = open("count.html", 'w')

s = ""
for line in file:
	s += line.replace('\n',' ').replace('.','').replace(',','')

arr = s.split(' ')

myDict = defaultdict(int)

for word in arr:
	myDict[word] += 1

stringy = ""
for k,v in sorted(myDict.iteritems(), key=lambda value: value[1]):
	if v > 0:
		stringy += str(v) + " "*(5-len(str(v))) + str(k) + '\n'

count.write(stringy)
