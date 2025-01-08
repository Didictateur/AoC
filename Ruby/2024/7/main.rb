require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

def parse(line)
  [line[0].chomp(':').to_i, line.drop(1).map(&:to_i)]
end

data = data.map { |line| parse(line) }
dataTest = dataTest.map { |line| parse(line) }

# Part 1

def hasResult(line)
  if line[1].length == 1
    return line[0] == line[1][0]
  end
  if hasResult([line[0], [line[1][0]+line[1][1]]+line[1].drop(2)])
    return true
  elsif hasResult([line[0], [line[1][0]*line[1][1]]+line[1].drop(2)])
    return true
  else
    return false
  end
end

def part1(data)
  score = 0
  data.each do |line|
    if hasResult(line)
      score += line[0]
    end
  end
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def hasNewResult(line)
  if line[1].length == 1
    return line[0] == line[1][0]
  end
  if hasNewResult([line[0], [line[1][0]+line[1][1]]+line[1].drop(2)])
    return true
  elsif hasNewResult([line[0], [line[1][0]*line[1][1]]+line[1].drop(2)])
    return true
  elsif hasNewResult([line[0], [line[1][0]*10**line[1][1].to_s.length+line[1][1]]+line[1].drop(2)])
    return true
  else
    return false
  end
end

def part2(data)
  score = 0
  data.each do |line|
    if hasNewResult(line)
      score += line[0]
    end
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"