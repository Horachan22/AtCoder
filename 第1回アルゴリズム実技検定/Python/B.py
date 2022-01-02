'''
===================================================================
Project Name  : 増減管理
File Name     : B.py
Encoding      : UTF-8
Creation Date : 2022/1/1
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
'''

def main():
	input_data = input()
	if input_data.isdigit() == True:
		print(int(input_data) * 2)
	else:
		print('error')

if __name__ == '__main__':
	main()
