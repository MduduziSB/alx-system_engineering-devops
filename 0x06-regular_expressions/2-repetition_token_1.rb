#!/usr/bin/env ruby
# Regular expression matching method
if ARGV.empty?
  exit 1
end
puts ARGV[0].scan(/hb?tn/).join
