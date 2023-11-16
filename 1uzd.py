#ievaditais skaitlis
ievaditais_skaitlis = int(input("Ievadiet skaitli: "))

summa = 0

for skaitlis in range(1, ievaditais_skaitlis + 1):
    summa += skaitlis

#rezultāts
print("Summa no 1 līdz", ievaditais_skaitlis, "ir:", summa)
