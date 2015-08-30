#!/usr/bin/ruby
# AOJ
# ALDS1_2_B
# Selection Sort

gets
n  = gets.split(' ').map{|i| i.to_i}
nl = n.length
ct = 0
for i in 0..nl-1
  min = i
  for j in (i+1)..nl-1
    if n[min] > n[j]
      min = j
    end
  end
  if i != min
    n[i], n[min] = n[min], n[i]
    ct += 1
  end
end

puts n.join ' '
puts ct
