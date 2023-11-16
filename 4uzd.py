def faktorials(skaitlis):
    rezultats = 1
    for i in range(1, skaitlis + 1):
        rezultats * i
    return rezultats

# Lietotāja ievade
ievade = int(input("Ievadiet skaitli, lai aprēķinātu faktoriālu: "))

# Aprēķina faktoriālu un izvada rezultātu
print(f"faktoriāls no {ievade} ir {faktorials(ievade)}")