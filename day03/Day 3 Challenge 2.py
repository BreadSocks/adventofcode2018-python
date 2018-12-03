grid = {}
total_claims = 0
ruined_claims = set()

with open("input.txt") as inputFile:
    for i, line in enumerate(inputFile):
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
                    previous_claim = grid[key]
                    ruined_claims.add(previous_claim)
                    ruined_claims.add(claim)
                else:
                    grid[key] = claim

        total_claims += 1

not_ruined = ""
for c in range(1, total_claims + 1):
    key = "#" + str(c)
    if key not in ruined_claims:
        not_ruined = key
print "Number of total claims:", len(ruined_claims), "Not ruined:", total_claims - len(ruined_claims), ":", not_ruined
