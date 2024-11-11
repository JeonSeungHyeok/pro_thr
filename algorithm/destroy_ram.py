def destroyed_ram(rams):
	count = 0
	dest_ram = []
	for i, ram in enumerate(rams):
		while not ram % 2:
			ram /= 2
			#print(ram)
		if ram > 1:
			count += 1
			dest_ram.append(i+1)
	print(count)
	if count:
		for d_ram in dest_ram:
			print(d_ram, end=' ')
			
def destroyed_ram2(rams):
	dest_ram = []
	count = 0

	for i, ram in enumerate(rams):
			if ram & (ram-1):
				count+=1
				dest_ram.append(i+1)
	print(count)
	if count:
		for d_ram in dest_ram:
			print(d_ram, end=' ')
				
def main():
	n = int(input())
	rams = list(map(int, input().split()))
	destroyed_ram2(rams)

if __name__=='__main__':
	main()
