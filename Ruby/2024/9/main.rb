require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
test = Parse.test(year, day, false)

def parse(line)
  line[0].split("").map(&:to_i)
end

data = parse(data[0])
test = parse(test[0])

# Part 1

def makeMemory(data)
  memory = []
  free = false
  id = 0
  data.each do |d|
    if free
      memory += [-1] * d
    else
      memory += [id] * d
      id += 1
    end
    free = !free
  end
  memory
end

def part1(data)
  score = 0
  mem = makeMemory(data)
  index = 0
  while mem[index] != nil
    if mem[index] == -1
      v = -1
      while v == -1
        v = mem.pop
      end
      score += index * v
    else
      score += index * mem[index]
    end
    index += 1
  end
  score
end

puts "Part 1:"
puts "  Test: #{part1(test)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  score = 0
  score
end

puts "Part 2:"
puts "  Test: #{part2(test)}"
puts "  Data: #{part2(data)}"