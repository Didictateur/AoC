require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

def parse(line)
  line[0].split("")#.map(&:to_i)
end

data.each_with_index { |line, index| data[index] = parse(line) }
dataTest.each_with_index { |line, index| dataTest[index] = parse(line) }

# Part 1

def colorit(data, division, i, j)
  neighbor = [
    [i+1, j],
    [i-1, j],
    [i, j+1],
    [i, j-1]
  ].select { |a, b| 0 <= a && a < division.length && 0 <= b && b < division[0].length }
  neighbor.each do |a, b|
    if division[a][b] == -1 && data[i][j] == data[a][b]
      division[a][b] = division[i][j]
      colorit(data, division, a, b)
    end
  end
end

def divide(data)
  division = Array.new(data.length) { Array.new(data[0].length) { -1 } }
  color = 0
  (0...data.length).each do |i|
    (0...data[0].length).each do |j|
      if division[i][j] == -1
        division[i][j] = color
        color += 1
        colorit(data, division, i, j)
      end
    end
  end
  division
end

def perimeter(positions, symbol)
  perim = 0
  (0...positions[symbol].length).each do |i|
    perim += 4
    (0...positions[symbol].length).each do |j|
      a, b = positions[symbol][i]
      c, d = positions[symbol][j]
      if (a - c)**2 + (b - d)**2 == 1
        perim -= 1
      end
    end
  end
  perim
end

def part1(data)
  score = 0
  positions = {}
  usedData = divide(data)
  (0...usedData.length).each do |i|
    (0...usedData[0].length).each do |j|
      if positions.keys.include?(usedData[i][j])
        positions[usedData[i][j]] << [i, j]
      else
        positions[usedData[i][j]] = [[i, j]]
      end
    end
  end
  
  positions.keys.each { |key| score += positions[key].length * perimeter(positions, key)}
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def findCorner(division, color)
  (0...division.length).each do |i|
    (0...division[0].length).each do |j|
      if division[i][j] == color
        return [i, j]
      end
    end
  end
  raise "color not find: #color"
end

def followPaht(division, color, i, j, dir, positions_init)
  score = 0
  # puts [i, j, dir, positions_init].inspect
  while positions_init != [i, j, dir]
    left = [i-dir[1], j+dir[0]]
    forward = [i+dir[0], j+dir[1]]

    if 0 <= left[0] && left[0] < division.length && 0 <= left[1] && left[1] < division[0].length && division[left[0]][left[1]] == color
      score += 1
      dir = [-dir[1], dir[0]]
      i, j = left[0], left[1]
    elsif 0 <= forward[0] && forward[0] < division.length && 0 <= forward[1] && forward[1] < division[0].length && division[forward[0]][forward[1]] == color
      i, j = forward[0], forward[1]
    else
      score += 1
      dir = [dir[1], -dir[0]]
    end
    # puts [i, j, dir, positions_init].inspect
  end
  score + 1
end

def get_area(division, color)
  area = 0
  (0...division.length).each do |i|
    (0...division[0].length).each { |j| area += division[i][j] == color ? 1 : 0 }
  end
  area
end

def part2(data)
  score = 0
  division = divide(data)
  saw = []
  (0...division.length).each do |i|
    (0...division[0].length).each do |j|
      if !saw.include?(division[i][j])
        saw << division[i][j]
        sides, area = followPaht(division, division[i][j], i, j, [0, 1], [i, j, [-1, 0]]), get_area(division, division[i][j])
        # puts [sides, area].inspect
        score += sides * area
      end
    end
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "TODO : penser aux parties encerclantes d'une zone"
# puts "  Data: #{part2(data)}"