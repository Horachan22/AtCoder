'''
===================================================================
Project Name  : 3番目
File Name     : C.py
Encoding      : UTF-8
Creation Date : 2022/1/3
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
'''

def main():
	input_data = input()
	sorted_data = input_data.split(' ')
	sorted_data = [int(i) for i in sorted_data]
	sorted_data.sort(reverse = True)
	print(sorted_data[2])

if __name__ == '__main__':
	main()
