require_relative '../../parse.rb'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, true)
test = Parse.test(year, day, true)

# Part 1

def part1(data)
  first = data.map { |row| row[0] }
  second = data.map { |row| row[1] }

  first = first.sort
  second = second.sort

  sum = 0
  first.each_with_index do |value, index|
    sum += (value - second[index]).abs
  end

  sum
end

puts "Part 1:"
puts "  Test: #{part1(test)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  first = data.map { |row| row[0] }
  second = data.map { |row| row[1] }

  score = 0
  first.each do |v1|
    it = 0
    second.each do |v2|
      if v1 == v2 
        it += 1
      end
    end
    score += v1 * it
  end

  score
end

puts "Part 2:"
puts "  Test: #{part2(test)}"
puts "  Data: #{part2(data)}"