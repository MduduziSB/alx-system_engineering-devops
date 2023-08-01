#!/usr/bin/env ruby
# Regular expression matching method

input_string = ARGV[0]

def regex_match(input)
  reg = /School/
  input.match reg
end
regex_match(input_string)
