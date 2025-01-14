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
  attr_accessor :a, :b, :price

  def initialize(a, b, price)
    @a = a
    @b = b
    @price = price
  end

  def find_price()
    det = @a[0]*@b[1] - @a[1] * @b[0]
    a = (@b[1] * @price[0] - @b[0] * @price[1]) / det
    b = (-@a[1] * @price[0] + @a[0] * @price[1]) / det
    if a*@a[0] + b*@b[0] == @price[0] && a*@a[1] + b*@b[1] == @price[1]
      return 3 * a + b
    end
    return 0
  end

  def display_info
    puts "A: #{@a}, B: #{@b}, Price: #{@price}"
  end
end

# Part 1

def parse_data(data, offset=0)
  machines = []
  m = []
  data.each do |line|
    if line[1] == "A:" || line[1] == "B:"
      m << [line[2][1..-1].to_i, line[3][1..-1].to_i]
    elsif line.length > 0
      m << [line[1][2..-1].to_i + offset, line[2][2..-1].to_i + offset]
      machines << Machin.new(m[0], m[1], m[2])
      m = []
    end
  end
  machines
end

def part1(data)
  score = 0
  machines = parse_data(data)
  machines.each { |m| score += m.find_price }
  score
end

puts "Part 1:"
puts "  Test: #{part1(dataTest)}"
puts "  Data: #{part1(data)}"

# Part 2

def part2(data)
  score = 0
  machines = parse_data(data, 10000000000000)
  machines.each { |m| score += m.find_price }
  score
end

puts "Part 2:"
puts "  Test: #{part2(dataTest)}"
puts "  Data: #{part2(data)}"