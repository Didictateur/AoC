require_relative '../../parse.rb'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
test = Parse.test(year, day, false)

# Part 1

def part1(data)
  score = 0
  score
end

puts "Part 1:"
puts "  Test: #{part1(test)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  score = 0
  score
end

puts "Part 2:"
puts "  Test: #{part2(test)}"
puts "  Data: #{part2(data)}"