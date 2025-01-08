require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
test = Parse.test(year, day, false)

def parse(line)
  line[0].split("").map(&:to_i)
end

data.each_with_index { |line, index| data[index] = parse(line) }
test.each_with_index { |line, index| test[index] = parse(line) }

# Part 1

def followTrack(data, multiplicities, i, j)
  if multiplicities[i][j].length == 0 # not visited yet
    heigh = data[i][j]
    if heigh == 9
      multiplicities[i][j] << [i, j]
    else
      multiplicities[i][j] << [-1, -1]
      neighbor = []
      [[i+1, j], [i-1, j], [i, j+1], [i, j-1]].each do |a, b|
        if 0 <= a && a < data.length && 0 <= b && b < data[0].length && data[a][b] == data[i][j] + 1
          neighbor << [a, b]
        end
      end
      neighbor.each do |a, b|
        followTrack(data, multiplicities, a, b)
        multiplicities[i][j] += multiplicities[a][b]
      end
    end
  end
end

def part1(data)
  score = 0
  multiplicities = Array.new(data.length) { Array.new(data[0].length) { [] } }
  (0...data.length).each { |i| (0...data[0].length).each { |j| followTrack(data, multiplicities, i, j) } }
  (0...data.length).each do |i|
    (0...data[0].length).each do |j|
      if data[i][j] == 0
        score += multiplicities[i][j].uniq.length - 1
      end
    end
  end
  score
end

puts "Part 1:"
puts "  Test: #{part1(test)}"
puts "  Data: #{part1(data)}"

# Part 2

def followTrails(data, rates, i, j)
  if rates[i][j] == -1 # not visited yet
    heigh = data[i][j]
    if heigh == 9
      rates[i][j] = 1
    else
      rates[i][j] = 0
      neighbor = []
      [[i+1, j], [i-1, j], [i, j+1], [i, j-1]].each do |a, b|
        if 0 <= a && a < data.length && 0 <= b && b < data[0].length && data[a][b] == data[i][j] + 1
          neighbor << [a, b]
        end
      end
      neighbor.each do |a, b|
        followTrails(data, rates, a, b)
        rates[i][j] += rates[a][b]
      end
    end
  end
end

def part2(data)
  score = 0
  rates = Array.new(data.length) { Array.new(data[0].length) { -1 } }
  (0...data.length).each { |i| (0...data[0].length).each { |j| followTrails(data, rates, i, j) } }
  (0...data.length).each do |i|
    (0...data[0].length).each do |j|
      if data[i][j] == 0
        score += rates[i][j]
      end
    end
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(test)}"
puts "  Data: #{part2(data)}"