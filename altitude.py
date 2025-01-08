
max = 0
sum = 0
gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]
for num in gain:
    sum = sum + num
    if sum > max:
        max = sum
    # sum = sum + num

print(max) 