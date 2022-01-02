=begin
===================================================================
Project Name  : 増減管理
File Name     : B.rb
Encoding      : UTF-8
Creation Date : 2022/1/2
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
=end

def main()
	n = gets().to_i()
	data_list = []
	for i in 0..n - 1 do
		input_data = gets().to_i()
		data_list.push(input_data)
	end

	for i in 1..n - 1 do
		diff = data_list[i] - data_list[i - 1]
		if diff == 0
			puts('stay')
		elsif diff > 0
			print('up ')
			puts(diff)
		else
			print('down ')
			puts(-diff)
		end
	end
end

if __FILE__ == $0
	main()
end
