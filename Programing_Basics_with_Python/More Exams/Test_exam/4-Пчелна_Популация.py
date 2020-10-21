population = int(input())
years = int(input())

started_population = population
new_bees = 0
died_bees = 0
ended_population = 0

for i in range(1, years+1):
    new_bees = (started_population // 10) * 2
    started_population = started_population + new_bees
    if i % 5 == 0:
        migrated_bees = (started_population // 50) * 5
        started_population = started_population - migrated_bees
    died_bees = (started_population // 20) * 2
    ended_population = started_population - died_bees
    started_population = ended_population
print(f"Beehive population: {ended_population:.0f}")