def solve(max)
    max -= 1
    nums = (1..max).find_all { |x| x % 3 == 0 or x % 5 == 0}
    nums.reduce(:+)
end

puts solve 10
puts solve 1000
