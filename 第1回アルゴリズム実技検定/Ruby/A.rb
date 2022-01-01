=begin
===================================================================
Project Name  : 2倍チェック
File Name     : A.rb
Encoding      : UTF-8
Creation Date : 2022/1/1
Copyright (c) 2022 Yuma Horaguchi All rights reserved.
===================================================================
=end

def main()
	input_data = gets()
	if /^[+-]?[0-9]+$/ =~ input_data.to_s
		puts(Integer(input_data) * 2)
	else
		puts('error')
	end
end

if __FILE__ == $0
	main()
end
