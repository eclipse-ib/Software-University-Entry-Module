obj_side_size = float(input("Въведете размер на едната страна на площадката: "))
plochka_w = float(input("Въведте широчината на плочката: "))
plochka_h = float(input("Въведете дължината на плочката: "))
peika_w = float(input("Въведете широчината на пейката: "))
peika_h = float(input("Въведете дължината на пейката: " ))

obj_size = obj_side_size * obj_side_size
plochka_size = plochka_w * plochka_h
peika_size = peika_w * peika_h

time_for_one_plochka = 0.2

obj_size_wo_peika = obj_size - peika_size
needed_plochki = obj_size_wo_peika / plochka_size
needed_time = needed_plochki * time_for_one_plochka

print("Общ брой необходими плочки = ", needed_plochki, "ще бъдат поставени за "
      , needed_time, "минути.")









