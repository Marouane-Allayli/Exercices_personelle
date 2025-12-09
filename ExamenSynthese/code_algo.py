
planetes = [
    ["Xenora", True, 23],
    ["Cryovus", False, -120],
    ["Solaria", True, 85],
    ["Aquinis", False, -30],
    ["Ignora", False, 14],
    ["Lunaris", True, 15],
    ["Zephyra", True, 42],
    ["Frostane", False, 21],
    ["Pyronis", False, 120],
    ["Vortera", True, 5],

    ["Meridion", False, 18],
    ["Umbraxis", True, -10],
    ["Helionis", False, 50],
    ["Crysalune", False, 12],
    ["Terranova", True, 17],
    ["Auroria", False, 40],
    ["Nebulys", False, 22],
    ["Glaciara", False, -80],
    ["Flareon", True, 95],
    ["Verdantis", False, 19],

    ["Obscurion", True, 8],
    ["Caeloria", False, 16],
    ["Rivandor", False, 25],
    ["Stormyra", False, 13],
    ["Vulkaria", True, 200],
    ["Ecoris", False, 20],
    ["Fjordalis", False, -5],
    ["Noctyra", True, 10],
    ["Solsticea", False, 15],
    ["Brumatis", False, 70],
]



Habitable = []
temperature_max = 0
planet_optimal = ""

for planete in planetes:
    nom = planete[0]
    habbiter = planete[1]
    temperature = planete[2]

    if habbiter == False and 12 < temperature < 22:
        Habitable.append(nom)
        if temperature > temperature_max:
            planet_optimal = nom
            temperature_max = temperature

print(Habitable)
print(planet_optimal)
print(temperature_max)