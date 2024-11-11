def bboyu(s,c):
	
	i=0
	while True:
		if s=='':
			break
		if s[i]*c == s[i:i+c]:
			temp = s[i]
			while s[i:i+1] == temp:
				s = s[:i]+s[i+1:]
			i=0
			continue
		elif i == len(s)-c:
			break
		i+=1
		
	if s:
		return ''.join(s)
	else:
		return 'CLEAR!'


def main():
	n,m = map(int, input().split())
	s = input()
	print(bboyu(s,m))

if __name__=='__main__':
	main()
