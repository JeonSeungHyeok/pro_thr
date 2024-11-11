def func(name):
	chname = ''
	for i in range(len(name)-1):
		if name[i] <= name[i+1]:
			chname += ''.join(name[i])
		else:
			chname += ''.join(name[i+1:])
			break
	return chname

def main():
	print(func(input()))

if __name__=='__main__':
	main()