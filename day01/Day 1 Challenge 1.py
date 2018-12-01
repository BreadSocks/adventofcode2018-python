frequency = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        line = line.replace("\n", "")
        number = int(line)
        frequency += number
print frequency
