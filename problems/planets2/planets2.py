# ships frequent to the spaceport
p = int(input()) #  2 <= p <= 15
species_to_planet = {}
visitors = {}
for i in range(p):
    inp = input().split()
    name, species = inp[0], inp[2:]
    visitors[name] = 0
    for s in species:
        species_to_planet[s] = name

v = int(input())
for i in range(v):
    inp = input().split()
    num, species = int(inp[0]), inp[1]

    planet = species_to_planet[species]
    visitors[planet] += num
keys = sorted(list(visitors.keys()))

for k in keys:
    print(k, visitors[k])