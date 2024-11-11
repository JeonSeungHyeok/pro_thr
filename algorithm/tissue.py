def main():
	count = 0
	n,m = map(int, input().split())
	tissue = list(map(int, input().split()))
	tissue_sum = sum(tissue)
	tissue_modify = (tissue_sum + m) // n
	for t in tissue:
		if tissue_modify < t:
			count = 1
	if count:
		print("No way!") 
	else:
		print(tissue_modify)
if __name__ == '__main__':
	main()

#---------------------------------------------------

def main():
	n,m = map(int, input().split())
	tissue = list(map(int, input().split()))
	tissue_sum = sum(tissue)
	tissue_modify = (tissue_sum + m) // n
	if any(tissue_modify < t for t in tissue):
		print("No way!") 
	else:
		print(tissue_modify)
if __name__ == '__main__':
	main()

#---------------------------------------------------

def main():
	n,m = map(int, input().split())
	tissue = list(map(int, input().split()))
	tissue_sum = sum(tissue)
	tissue_modify = (tissue_sum + m) // n
	print("No way!" if any(tissue_modify < t for t in tissue)	else tissue_modify)
	
if __name__ == '__main__':
	main()
