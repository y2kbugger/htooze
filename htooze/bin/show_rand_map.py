import htooze
p = htooze.world.Planet((21, 21))
for n in range(12):
    c = htooze.world.Cell()
    p.addcell(c)

rows = [['z' if (x, y) in p.life.keys() else '-' for x in range(p.size[0])] for y in range(p.size[0])]

out = "\n".join([" ".join([c for c in row]) for row in rows])
print(out)
