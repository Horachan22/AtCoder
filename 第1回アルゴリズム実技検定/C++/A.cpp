/*
===================================================================
Project Name  : 2倍チェック
File Name     : A.cpp
Encoding      : UTF-8
Creation Date : 2022/1/1
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
*/

#include <iostream>
#include <cctype>
#include <algorithm>

int main(){
	std::string input_data;
	std::cin >> input_data;
	if(std::all_of(input_data.cbegin(), input_data.cend(), isdigit)){
		std::cout << stoi(input_data) * 2 << std::endl;
	}
	else{
		std::cout << "error" << std::endl;
	}
	return 0;
}
