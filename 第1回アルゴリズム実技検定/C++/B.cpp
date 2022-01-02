/*
===================================================================
Project Name  : 増減管理
File Name     : B.cpp
Encoding      : UTF-8
Creation Date : 2022/1/2
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
*/

#include <iostream>
#include <vector>

using namespace std;

int main(){
	int n;
	vector<int> data_list;
	cin >> n;
	for(int i = 0; i < n; i++){
		int input_data;
		cin >> input_data;
		data_list.push_back(input_data);
	}

	int diff = 0;
	for(int i = 1; i < n; i++){
		diff = data_list[i] - data_list[i - 1];
		if(diff == 0){
			cout << "stay" << endl;
		}
		else if(diff > 0){
			cout << "up " << diff << endl;
		}
		else{
			cout << "down " << -diff << endl;
		}
	}
	return 0;
}
