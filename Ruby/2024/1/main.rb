require_relative '../../parse.rb'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, true)
dataTest = Parse.dataTest(year, day, true)

# Part 1

def part1(data)
  t1 = data.map { |row| row[0] }
  t2 = data.map { |row| row[1] }

  t1 = t1.sort
  t2 = t2.sort

  t1.zip(t2).map { |a, b| (a - b).abs }.sum

end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  t1 = data.map { |row| row[0] }
  t2 = data.map { |row| row[1] }

  score = 0
  t1.each { |v1| score += v1 * t2.count(v1) }

  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"