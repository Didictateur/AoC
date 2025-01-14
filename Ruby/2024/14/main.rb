require_relative '../../parse.rb'
require 'tty-progressbar'

year = ARGV[0]
day = ARGV[1]

data = Parse.data(year, day, false)
dataTest = Parse.dataTest(year, day, false)

# def parse(line)
#   line[0].split("")#.map(&:to_i)
# end

# data.each_with_index { |line, index| data[index] = parse(line) }
# dataTest.each_with_index { |line, index| dataTest[index] = parse(line) }

class Machin
  attr_accessor :x, :y, :vx, :vy, :xmax, :ymax

  def initialize(line, size_max)
    @xmax = size_max[0]
    @ymax = size_max[1]

    line[0].to_s.scan(/p=(\d+),(\d+)/).each { |b, a| @x, @y = a.to_i, b.to_i }
    line[1].to_s.scan(/v=(-?\d+),(-?\d+)/).each { |b, a| @vx, @vy = a.to_i, b.to_i }
    # puts [@x, @y, @vx, @vy].inspect
  end

  def step(step)
    x = (@x + step * @vx) % @xmax
    y = (@y + step * @vy) % @ymax
    return [x, y]
  end
end

# Part 1

def part1(data)
  score = 1
  size_max = data.length < 20 ? [7, 11] : [103, 101]
  machines = []
  data.each do |line|
    if line.length > 0
      # puts line.inspect
      machines << Machin.new(line, size_max)
    end
  end
  positions = []
  machines.each { |m| positions << m.step(100) }
  # puts positions.inspect
  safety = []
  safety << positions.select { |x, y| 0 <= x && x < size_max[0]/2 && 0 <= y && y < size_max[1]/2 }.length
  safety << positions.select { |x, y| 0 <= x && x < size_max[0]/2 && size_max[1]/2 < y && y < size_max[1]}.length
  safety << positions.select { |x, y| size_max[0]/2 < x && x < size_max[0] && 0 <= y && y < size_max[1]/2 }.length
  safety << positions.select { |x, y| size_max[0]/2 < x && x < size_max[0] && size_max[1]/2 < y && y < size_max[1]}.length
  # puts safety.inspect
  safety.each { |s| score *= s }
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2
def draw(machines, step, size_max)
  drawing = Array.new(size_max[0]) { Array.new(size_max[1], '.') }
  machines.each do |machin|
    x, y = machin.step(step)
    drawing[x][y] = 'X'
  end
  drawing.each do |line|
    puts line.join(' ')
  end
end

def part2(data)
  score = 0
  score = 1
  size_max = data.length < 20 ? [7, 11] : [103, 101]
  machines = []
  data.each do |line|
    if line.length > 0
      # puts line.inspect
      machines << Machin.new(line, size_max)
    end
  end
  step_max = size_max[0]*size_max[1] #it's repeating
  (0...step_max).each do |step|
    system("clear")
    draw(machines, step, size_max)
    puts step
    sleep(0.01)
  end
  step_max-1
end

puts "Part 2:"
# puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"