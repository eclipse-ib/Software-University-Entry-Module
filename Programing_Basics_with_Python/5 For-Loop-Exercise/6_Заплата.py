opened_tabs = int(input())
sallary = int(input())

for i in range(1, opened_tabs+1):
    tab = input()
    if tab == "Facebook":
        sallary -= 150
    elif tab == "Instagram":
        sallary -= 100
    elif tab == "Reddit":
        sallary -= 50
    if sallary <= 0:
        print(f"You have lost your salary.")
        exit()
print(f"{sallary}")