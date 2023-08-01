def max(array)
  largest = array[0]

  array.each do |number|
    if number > largest
      largest = number
    end
  end

  return largest
end

p max([5, 17, -4, 8, 12])