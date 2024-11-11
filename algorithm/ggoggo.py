# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def main():
	vowels = 'aeiouAEIOU'
	result = []
	input_N = int(input())
	
	for _ in range(input_N):
		input_str = input()
		find_vowels = [ch for ch in input_str if ch in vowels]
		
		if find_vowels:
			result.append(''.join(find_vowels))
		else:
			result.append('???')
			
	print('\n'.join(result))

if __name__ == '__main__':
	main()