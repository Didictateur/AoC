module Parse
  def self.data(year, day, int=false)
    data = File.open("#{year}/#{day}/data.txt", "r")
    lines = data.readlines.map do |line|
      line.chomp.split(" ")
    end
    data.close
    int ? lines.map { |line| line.map(&:to_i) } :
    lines
  end

  def self.test(year, day, int=false)
    data = File.open("#{year}/#{day}/test.txt", "r")
    lines = data.readlines.map do |line|
      line.chomp.split(" ")
    end
    data.close
    int ? lines.map { |line| line.map(&:to_i) } :
    lines
  end
end