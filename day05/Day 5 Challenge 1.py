units = list(open("input.txt").read())
new_units = [units[0]]

index = 1

while index < len(units):
    unit = units[index]
    if len(new_units) == 0:
        new_units.append(unit)
    else:
        previous_unit = new_units[-1]
        if unit.lower() == previous_unit.lower() and unit != previous_unit:
            new_units.pop()
        else:
            new_units.append(unit)
    index += 1

print len(new_units)
