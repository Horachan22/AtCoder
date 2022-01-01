/*
===================================================================
Project Name  : 2倍チェック
File Name     : A.go
Encoding      : UTF-8
Creation Date : 2022/1/1
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
*/

package main

import (
	"fmt"
	"strconv"
)

func main() {
	var input_data string
	var int_data int
	fmt.Scan(&input_data)
	int_data, _ = strconv.Atoi(input_data)
	if int_data != 0 || input_data == "000" {
		fmt.Printf("%v\n", int_data*2)
	} else {
		fmt.Printf("error\n")
	}
}
