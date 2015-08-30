#!/usr/bin/ruby
# AOJ
# ALDS1_2 C
# Stable Sort

def buble_sort(cards)
  c  = cards
  cl = c.length
  (0).upto(cl-1) do |i|
    (cl-1).downto(i+1) do |j|
      if c[j-1][1] > c[j][1]
        c[j-1], c[j] = c[j], c[j-1]
      end
    end
  end
  c
end

def select_sort(cards)
  c  = cards
  cl = c.length
  for i in 0..cl-1
    min = i
    for j in i..cl-1
      if c[j][1] < c[min][1]
        min = j
      end
    end
    c[i], c[min] = c[min], c[i]
  end
  c
end

def stable?(origin, card_info)
  origin_info = []
  origin.map do |o|
    tmp = o.split ''
    origin_info << [tmp[0], tmp[1]]
  end

  for ci in card_info
    o_index = 0
    loop do
      if origin_info[o_index][1] == ci[1]
        if origin_info[o_index][0] != ci[0]
          return false
        end
        origin_info.delete origin_info[o_index]
        break
      end
      o_index += 1
    end
  end
  true
end

gets
origin = gets.split ' '
card_info1 = []
card_info2 = []
origin.map do |card|
  tmp = card.split ''
  card_info1 << [tmp[0], tmp[1]]
  card_info2 << [tmp[0], tmp[1]]
end

# Bubble Sort
puts buble_sort(card_info1).map{|m, n| [m, n].join ''}.join ' '
if stable? origin, card_info1 then puts 'Stable' else puts 'Not stable' end

# Select Sort
puts select_sort(card_info2).map{|m, n| [m, n].join ''}.join ' '
if stable? origin, card_info2 then puts 'Stable' else puts 'Not stable' end
