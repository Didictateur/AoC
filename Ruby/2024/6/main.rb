require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

# Part 1

def find_guard(data)
  data.each_with_index do |line, i|
    line.each_with_index do |char, j|
      if char == '^'
        return [i, j]
      end
    end
  end
  raise "No guard found"  
end

def travel(gi, gj, dir, data, square)
  square << [gi, gj]
  case dir
  when 'U'
    if gi == 0
      return square
    elsif data[gi - 1][gj] == '#'
      return travel(gi, gj, 'R', data, square)
    else
      return travel(gi - 1, gj, dir, data, square)
    end
  when 'R'
    if gj == data[0].length - 1
      return square
    elsif data[gi][gj + 1] == '#'
      return travel(gi, gj, 'D', data, square)
    else
      return travel(gi, gj + 1, dir, data, square)
    end
  when 'D'
    if gi == data.length - 1
      return square
    elsif data[gi + 1][gj] == '#'
      return travel(gi, gj, 'L', data, square)
    else
      return travel(gi + 1, gj, dir, data, square)
    end
  when 'L'
    if gj == 0
      return square
    elsif data[gi][gj - 1] == '#'
      return travel(gi, gj, 'U', data, square)
    else
      return travel(gi, gj - 1, dir, data, square)
    end
  end
  raise "Invalid direction"
end

def part1(data)
  score = 0
  data.each_with_index { |line, index| data[index] = line[0].split('') }
  gi, gj = find_guard(data)
  squares = travel(gi, gj, 'U', data, [])
  score = squares.uniq.length
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def islooping(gi, gj, dir, data, obstacles)
  if obstacles[gi][gj].include?(dir)
    return true
  end
  obstacles[gi][gj] << dir
  case dir
  when 'U'
    if gi == 0
      return false
    elsif data[gi - 1][gj] == '#'
      return islooping(gi, gj, 'R', data, obstacles)
    else
      return islooping(gi - 1, gj, 'U', data, obstacles)
    end
  when 'R'
    if gj == data[0].length - 1
      return false
    elsif data[gi][gj + 1] == '#'
      return islooping(gi, gj, 'D', data, obstacles)
    else
      return islooping(gi, gj + 1, 'R', data, obstacles)
    end
  when 'D'
    if gi == data.length - 1
      return false
    elsif data[gi + 1][gj] == '#'
      return islooping(gi, gj, 'L', data, obstacles)
    else
      return islooping(gi + 1, gj, 'D', data, obstacles)
    end
  when 'L'
    if gj == 0
      return false
    elsif data[gi][gj - 1] == '#'
      return islooping(gi, gj, 'U', data, obstacles)
    else
      return islooping(gi, gj - 1, 'L', data, obstacles)
    end
  end
  raise "Invalid direction"
end

def part2(data)
  score = 0

  gi, gj = find_guard(data)
  squares = travel(gi, gj, 'U', data, []).uniq

  total_iterations = data.length * data[0].length
  bar = TTY::ProgressBar.new("Progress [:bar] :percent :eta", total: total_iterations)

  (0...data.length).each do |i|
    (0...data[0].length).each do |j|
      datacpy = data.map(&:dup)
      if datacpy[i][j] == '.' and squares.include?([i, j])
        datacpy[i][j] = '#'
        obstacles = Array.new(data.length) { Array.new(data[0].length) { [] } }
        if islooping(gi, gj, 'U', datacpy, obstacles)
          score += 1
        end
      end
      bar.advance
    end
  end
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"