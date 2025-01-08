require_relative '../../parse.rb'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

(0..data.size).each do |i|
  data[i] = data[i][0].chars unless data[i].nil?
end

(0..dataTest.size).each do |i|
  dataTest[i] = dataTest[i][0].chars unless dataTest[i].nil?
end

# Part 1

def part1(data)
  score = 0
  (0...data.size).each do |i|
    (0...data[0].size).each do |j|
      if i + 3 < data.size && ["XMAS", "SAMX"].include?([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]].join)
        score += 1
      end
      if i + 3 < data.size && j + 3 < data[0].size && ["XMAS", "SAMX"].include?([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]].join)
        score += 1
      end
      if i + 3 < data.size && j - 3 >= 0 && ["XMAS", "SAMX"].include?([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]].join)
        score += 1
      end
      if j + 3 < data[0].size && ["XMAS", "SAMX"].include?([data[i][j], data[i][j+1], data[i][j+2], data[i][j+3]].join)
        score += 1
      end
    end
  end
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  score = 0
  (1...(data.size-1)).each do |i|
    (1...(data[0].size-1)).each do |j|
      if ["MAS", "SAM"].include?([data[i-1][j-1], data[i][j], data[i+1][j+1]].join) && ["MAS", "SAM"].include?([data[i+1][j-1], data[i][j], data[i-1][j+1]].join)
        score += 1
      end
    end
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"