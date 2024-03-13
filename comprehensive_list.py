# prints value from 1 to 100
sample_list=[num for num in range(1,101)]
print(sample_list)

# prints value from 1 to 100 excluding number divisible by 4
sample_list=[num for num in range(1,101) if num%4!=0]
print(sample_list)



values = [[3 - x for x in range(2)] for y in range(5)]
print(values)
#o/p [[3, 2], [3, 2], [3, 2], [3, 2], [3, 2]]

sum = 0.0
for row in values:
  for cell in row:
    sum += cell

print(sum)