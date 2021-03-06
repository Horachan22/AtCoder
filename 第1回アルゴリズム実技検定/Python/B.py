'''
===================================================================
Project Name  : 増減管理
File Name     : B.py
Encoding      : UTF-8
Creation Date : 2022/1/2
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
'''

def main():
	n = int(input())
	data_list = []
	for i in range(n):
		input_data = int(input())
		data_list.append(input_data)

	for i in range(1, n):
		diff = data_list[i] - data_list[i - 1]
		if diff == 0:
			print('stay')
		elif diff > 0:
			print('up', diff)
		else:
			print('down', -diff)

if __name__ == '__main__':
	main()
