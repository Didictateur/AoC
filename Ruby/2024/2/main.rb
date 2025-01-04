require_relative '../../parse.rb'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, true)
test = Parse.test(year, day, true)

# Part 1

def valide(a, b)
  1 <= a - b && a - b <= 3
end

def part1(data)
  score = 0
  data.each do |row|
    if row.each_cons(2).all? { |a, b| valide(a, b) }
      score += 1
    elsif row.each_cons(2).all? { |a, b| valide(b, a) }
      score += 1
    end
  end
  score
end

puts "Part 1:"
puts "  Test: #{part1(test)}"
puts "  Data: #{part1(data)}"

# Part 2

def remove_element(data, index)
  new_data = data.dup
  new_data.delete_at(index)
  new_data
end

def part2(data)
  score = 0
  data.each do |row|
    valide = false
    (0...row.size).each do |i|
      modified_row = remove_element(row, i)
      if modified_row.each_cons(2).all? { |a, b| 1 <= a - b and a - b <= 3 }
        valide = true
      end
      if modified_row.each_cons(2).all? { |a, b| 1 <= b - a and b - a <= 3 }
        valide = true
      end
    end
    score += valide ? 1 : 0
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(test)}"
puts "  Data: #{part2(data)}"