require_relative '../../parse.rb'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

def getrul(data)
  rules = []
  data.each do |line|
    line.to_s.scan(/(\d+)\|(\d+)/).each do |a, b|
      rules << [a.to_i, b.to_i]
    end
  end
  rules
end

def getlist(data)
  list = []
  data.each do |line|
    if line.to_s.match?(/.,./)
      list << line.to_s.gsub(/[\[\]\"]/, '').split(',').map(&:to_i)
    end
  end
  list
end

def respect(rules, update)
  (0...update.length).each do |i|
    ((i+1)...update.length).each do |j|
      if rules.include?([update[j], update[i]])
        return 0
      end
    end
  end
  update[(update.length/2)]
end

# Part 1

def part1(data)
  score = 0
  rules = getrul(data)
  list = getlist(data)

  list.each do |update|
    score += respect(rules, update)
  end
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def compare(a, b, rules)
  if rules.include?([a, b]) # a < b
    return -1
  elsif rules.include?([b, a]) # a > b
    return 1
  else
    return 0 # a ~ b
  end
end

def sort(update, rules)
  update.sort { |a, b| compare(a, b, rules) }
end

def part2(data)
  score = 0
  rules = getrul(data)
  list = getlist(data)
  list.each do |update|
    if respect(rules, update).zero?
      score += sort(update, rules)[(update.length/2)]
    end
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"