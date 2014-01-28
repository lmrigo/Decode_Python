input = "123456789"
input2 = "123454321"

def decode (num):
	return chr(int(num) + 96)

def translate (input):
	if len(input) == 1:
		return decode(input[0])
	else:
		return decode(input[0]) + translate(input[1:])

print translate(input2)

def morphAs(translated):
	result = []
	comboA = ['aa','ab','ac','ad','ae','af','ag','ah','ai']
	replaceA = ['k','l','m','n','o','p','q','r','s']
	n = 0
	for i in range(len(translated)-1):
		for j in range(len(comboA)):
			if (translated[i]+translated[i+1]) == comboA[j]:
				x = translated.replace(comboA[j],replaceA[j])
				result += ['']
				result[n] = x
				n += 1
	return result
print morphAs(translate(input2))

def morphBs(translated):
	result = []
	comboB = ['ba','bb','bc','bd','be','bf']
	replaceB = ['u','v','w','x','y','z']
	n = 0
	for i in range(len(translated)-1):
		for j in range(len(comboB)):
			if (translated[i]+translated[i+1]) == comboB[j]:
				x = translated.replace(comboB[j],replaceB[j])
				result += ['']
				result[n] = x
				n += 1
	return result
print morphBs(translate(input2))


"""
def possibilities (input)
	if (input[0] == '1') or (input[0] == '2'):
		return [translate(input,False),translate(input,True)]
	else:
		return


def translateLoop (input):
	result = ['']
	n = 0
	for i in range(len(input)):
		if(input[i] == '1') or (input[i] == '2'):
			result[n] += translate(input[i:])
			result += ['']
			n += 1
			result[n] += decode(input[i]+input[i+1])
		else:
			result[n] += translate(input[i:])
	return result
"""