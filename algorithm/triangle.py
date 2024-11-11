# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def main():
	x, y = [], []
	for _ in range(3):
		point_x, point_y = map(int, input().split())
		x.append(point_x)
		y.append(point_y)
	
	result = abs((x[0]*y[1] - x[1]*y[0] + x[1]*y[2] - x[2]*y[1] + x[2]*y[0] - x[0]*y[2])) / 2
	print(f'{result:.2f}')
	


if __name__=='__main__':
	main()
