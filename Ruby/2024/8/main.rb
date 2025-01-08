require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

def parse(line)
  line[0].split("")
end

data = data.map { |line| parse(line) }
dataTest = dataTest.map { |line| parse(line) }

# Part 1

def makeDictionnary(data)
  dic = {}
  (0...data.length).each do |i|
    (0...data[i].length).each do |j|
      if data[i][j] != '.'
        if dic.keys.include?(data[i][j])
          dic[data[i][j]] << [i, j]
        else
          dic[data[i][j]] = [[i, j]]
        end
      end
    end
  end
  dic
end

def findNodes(antennasList)
  nodes = []
  antennasList.each() do |x1, y1|
    antennasList.each() do |x2, y2|
      if x1 != x2 && y1 != y2
        nodes << [2 * x2 - x1, 2 * y2 - y1]
      end
    end
  end
  nodes
end

def part1(data)
  score = 0
  antennas = makeDictionnary(data)
  nodes = []
  antennas.each { |key, value| nodes += findNodes(value) }
  score = nodes.uniq.select { |i, j| (0...data.length).include?(i) && (0...data[0].length).include?(j) }.length
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def findAllNodes(antennasList, iMax, jMax)
  nodes = []
  antennasList.each() do |x1, y1|
    antennasList.each() do |x2, y2|
      if x1 != x2 && y1 != y2
        (0...[iMax, jMax].max).each do |n|
          nodes << [x2 + n*(x2-x1), y2 + n*(y2-y1)]
        end
      end
    end
  end
  nodes
end

def part2(data)
  score = 0
  antennas = makeDictionnary(data)
  nodes = []
  antennas.each { |key, value| nodes += findAllNodes(value, data.length, data[0].length) }
  score = nodes.uniq.select { |i, j| (0...data.length).include?(i) && (0...data[0].length).include?(j) }.length
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"