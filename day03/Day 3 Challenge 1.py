grid = {}

with open("input.txt") as inputFile:
    for line in inputFile:
        parts = line.split(" ")
        location = parts[2].strip(":").split(",")
        size = parts[3].split("x")

        claim = parts[0]
        from_left_edge = int(location[0])
        from_top_edge = int(location[1])
        width = int(size[0])
        height = int(size[1])

        for y in range(from_top_edge, from_top_edge + height):
            for x in range(from_left_edge, from_left_edge + width):
                key = x, y
                if key in grid:
                    grid[key] = "X"
                else:
                    grid[key] = claim

        # print "claim:", claim, "left:", from_left_edge, "top:", from_top_edge, "w:", width, "h:", height

print grid.values().count("X")
