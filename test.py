input1 = "1"
input2 = "11"
input3 = "111"
input4 = "1111"
input5 = "11111"
input6 = "111111"

lowercaseOffset = 96
def decode (strNum):
	return chr(int(strNum) + lowercaseOffset)

def translate (input):
	if len(input) < 1:
		return ""
	elif len(input) == 1:
		return decode(input[0])
	elif (input[0]+input[1]) == "10":
		return decode(input[0]+input[1]) + translate(input[2:])
	else:
		return decode(input[0]) + translate(input[1:])

#print translate(input4)

#comboA = {'aa':'k','ab':'l','ac':'m','ad':'n','ae':'o','af':'p','ag':'q','ah':'r','ai':'s'}
#comboB = {'ba':'u','bb':'v','bc':'w','bd':'x','be':'y','bf':'z'}
comboA = ['aa','ab','ac','ad','ae','af','ag','ah','ai']
comboB = ['ba','bb','bc','bd','be','bf']
def counter (translated,previousAB):
	if len(translated) <= 1:
		return 1.0
	duet = translated[0]+translated[1]
	if duet in comboA or duet in comboB:
		if previousAB:
			return (3.0/2.0) * counter(translated[1:],False)
		else:
			return 2.0 * counter(translated[1:],True)
	else:
		return counter(translated[1:],False)

print 'input1:  1<=>' + str(int(counter(translate(input1),False))) + '\t' + str(counter(translate(input1),False) == 1.0) 
print 'input2:  2<=>' + str(int(counter(translate(input2),False))) + '\t' + str(counter(translate(input2),False) == 2.0) 
print 'input3:  3<=>' + str(int(counter(translate(input3),False))) + '\t' + str(counter(translate(input3),False) == 3.0) 
print 'input4:  5<=>' + str(int(counter(translate(input4),False))) + '\t' + str(counter(translate(input4),False) == 5.0) 
print 'input5:  6<=>' + str(int(counter(translate(input5),False))) + '\t' + str(counter(translate(input5),False) == 6.0) 
print 'input6: 13<=>' + str(int(counter(translate(input5),False))) + '\t' + str(counter(translate(input5),False) == 13.0)


"""
input1 = "1"
input2 = "11"
input3 = "111"
input4 = "1111"
input5 = "11111"
input6 = "111111"

1
a
1
2
aa
k
2
3
aaa
a k
k a
3
4
aaaa
aa k
a ka
 kaa
 k k
5
5
aaaaa
aaa k
aa ka
a kaa
a k k
 kaaa
 ka k
 k ka
8
6
aaaaaa
aaaa k
aaa ka
aa kaa
aa k k
a kaaa
a ka k
a k ka
 kaaaa
 kaa k
 ka ka
 k kaa
 k k k
13

"""
""" 
next solution
4
aaaa = 1
1+aa k,3 = 1
1+a ka,2 = 1
1+ kaa,1 = 1
1+ k k,3 = 1


aa k
a ka
 kaa
 k k
5
"""