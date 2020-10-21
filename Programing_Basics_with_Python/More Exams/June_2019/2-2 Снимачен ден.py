time_for_shooting = int(input())
scenes = int(input())
scene_time = int(input())

day_time_for_shooting = (scenes * scene_time) + (time_for_shooting * 0.15)

left_time = time_for_shooting - day_time_for_shooting

if left_time >= 0:
    print(f"You managed to finish the movie on time! You have {round(abs(left_time))} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(abs(left_time))} minutes.")