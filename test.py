input = "123456789"
input2 = "123454321"
input3 = "12345678910"
input4 = "1234567891011"
input5 = "1101211"

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
def counter (translated,m):
	if len(translated) <= 1:
		return 0
	duet = translated[0]+translated[1]
	if duet in comboA or duet in comboB:
		return 2 + counter(translated[1:],0)
	else:
		return counter(translated[1:],0)

print input5 # 1101211
print translate(input5) # ajabaa
print counter(translate(input5),0) # 6
"""
1. ajabaa
2. ajabk
3. ajaua
4. ajlaa
5. ajlk
"""
"""
print input4 # 1234567891011
print translate(input4) # abcdefghijaa
print counter(translate(input4),0) # 6
1. abcdefghijaa
2. abcdefghijk
3. lcdefghijaa
4. lcdefghijk
5. awdefghijaa
6. awdefghijk
"""