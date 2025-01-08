require_relative '../../parse.rb'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

# Part 1

def part1(data)
  score = 0
  data.each do |line|
    line.to_s.scan(/mul\((\d{1,3}),(\d{1,3})\)/).each { |a, b| score += a.to_i * b.to_i }
  end
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  score = 0
  enable = 1
  data.each do |line|
    line.to_s.scan(/mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))/).each do |match|
      if match[0] && match[1]
        score += enable * match[0].to_i * match[1].to_i
      elsif match[2]
        enable = 1
      elsif match[3]
        enable = 0
      end
    end
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"