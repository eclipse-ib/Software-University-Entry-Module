bees = int(input())
flowers = int(input())

honey_by_bees = (bees * flowers) * 0.21

filled_honeycombs = honey_by_bees // 100

left_honey = honey_by_bees - filled_honeycombs*100

print(f"{filled_honeycombs:.0f} honeycombs filled.")
print(f"{left_honey:.2f} grams of honey left.")

