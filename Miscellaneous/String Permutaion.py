
def permute(string):
	if len(string)==2:
		output=[]
		output.append(string[0])
		output.append(string[1])
		output.append(string)
		return output
	else:
		output=[]

		output.append(permute(string[1:]))
		return output

print(permute('abc'))