from collections import defaultdict

def find_size(sizes):
	count_dict = defaultdict(int)
	
	for size in sizes:
		for x in range(size - 2, size + 3):
			count_dict[x] += 1

	max_count = max(count_dict.values())
	size_value = min(key for key, value in count_dict.items() if value == max_count)
	
	return size_value

def main():
	n = int(input())
	light = list(map(int, input().split()))
	dark = list(map(int, input().split()))

	light_avg = find_size(light)
	dark_avg = find_size(dark)

	print(light_avg, dark_avg)

	print("good" if light_avg > dark_avg else "bad")

if __name__ == "__main__":
	main()
