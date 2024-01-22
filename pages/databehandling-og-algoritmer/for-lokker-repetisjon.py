skuespillere = [
    {"name": "Tom Hanks", "age": 66},
    {"name": "Meryl Streep", "age": 73},
    {"name": "Leonardo DiCaprio", "age": 48},
    {"name": "Julia Roberts", "age": 55},
    {"name": "Denzel Washington", "age": 67},
    {"name": "Nicole Kidman", "age": 55},
    {"name": "Brad Pitt", "age": 59},
    {"name": "Charlize Theron", "age": 47},
    {"name": "Johnny Depp", "age": 59},
    {"name": "Emma Stone", "age": 34},
]

# Oppgaver:
# 1: Print navnet til Tom Hanks
# print(actors[0]["name"])
# # 2: Print alderen til Tom Hanks
# print(actors[0]["age"])

# brukerinput = int(input("Gi meg et nummer: "))
# brukerinput = 1
# print(actors[brukerinput]["name"])

størst = float("-inf")
størst_navn = "tullenavn"
for actor in actors:
    print(f"{actor['name']} er {actor['age']} år gammel")
    if actor["age"] > størst:
        størst = actor["age"]
        størst_navn = actor["name"]

print(f"Den eldste skuespilleren er {størst_navn} som er {størst} år gammel")



eldst = skuespillere[0]
for skuespiller in skuespillere[1:]:
    if actor['age'] > eldst['age']:
        eldst = actor

print(f"Den eldste skuespilleren er {eldst['name']} som er {eldst['age']} år gammel")
