input1 = "123456789"
input2 = "123454321"
input3 = "12345678910"
input4 = "1234567891011"
input5 = "1101211"
input6 = "11111"

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

print 'input1:' + str(counter(translate(input1),False) == 3.0) + ' 3<=>' + str(counter(translate(input1),False))
print 'input2:' + str(counter(translate(input2),False) == 6.0) + ' 6<=>' + str(counter(translate(input2),False))
print 'input3:' + str(counter(translate(input3),False) == 3.0) + ' 3<=>' + str(counter(translate(input3),False))
print 'input4:' + str(counter(translate(input4),False) == 6.0) + ' 6<=>' + str(counter(translate(input4),False))
print 'input5:' + str(counter(translate(input5),False) == 5.0) + ' 5<=>' + str(counter(translate(input5),False))
print 'input6:' + str(counter(translate(input5),False) == 5.0) + ' ?<=>' + str(counter(translate(input5),False))

"""
input1 = "123456789"
input2 = "123454321"
input3 = "12345678910"
input4 = "1234567891011"
input5 = "1101211"
input6 = "11111"
"""
