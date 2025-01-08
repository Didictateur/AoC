require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, true)
dataTest = Parse.dataTest(year, day, true)

# def parse(line)
#   line[0].split("").map(&:to_i)
# end

# data.each_with_index { |line, index| data[index] = parse(line) }
# dataTest.each_with_index { |line, index| dataTest[index] = parse(line) }

data = data[0]
dataTest = dataTest[0]

# Part 1

def compute(n, it, count)
  return count[[n, it]] if count.include?([n, it])

  if it == 0
    count[[n, 0]] = 1
    return 1
  end

  if n == 0
    count[[0, it]] = compute(1, it - 1, count)
  elsif n.to_s.length % 2 == 0
    str = n.to_s
    mid = str.length/2
    count[[n, it]] =
      compute(str[0...mid].to_i, it - 1, count) +
      compute(str[mid...(str.length)].to_i, it - 1, count)
  else
    count[[n, it]] = compute(2024 * n, it - 1, count)
  end
  return count[[n, it]]
end

def part1(data)
  score = 0
  count = {}
  data.each { |n| score += compute(n, 25, count) }
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  score = 0
  count = {}
  data.each { |n| score += compute(n, 75, count) }
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"