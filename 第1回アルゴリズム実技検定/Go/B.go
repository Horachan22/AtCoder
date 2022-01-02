/*
===================================================================
Project Name  : 増減管理
File Name     : A.go
Encoding      : UTF-8
Creation Date : 2022/1/2
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
*/

package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	data_list := []int{}
	for i := 0; i < n; i++ {
		var input_data int
		fmt.Scan(&input_data)
		data_list = append(data_list, input_data)
	}

	var diff int
	for i := 1; i < n; i++ {
		diff = data_list[i] - data_list[i-1]
		if diff == 0 {
			fmt.Printf("stay\n")
		} else if diff > 0 {
			fmt.Printf("up %v\n", diff)
		} else {
			fmt.Printf("down %v\n", -diff)
		}
	}
}
