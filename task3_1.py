count = 0
for x in range(1500, 2701):
    if x%7 == 0 and x%5 == 0:
        print(x)
        count += 1
print(count)
