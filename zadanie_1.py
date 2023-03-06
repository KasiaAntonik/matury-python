# Zadanie 1. Firma zdecydowała dać bonus 5% pracownikom, których rok pracy jest dłuższy niż 5 lat. Napisz program, który poprosi użytkownika o podanie: lat pracy oraz wynagrodzenia, i wyświetli kwotę bonusu, która się mu należy.

wynagrodzenie = int(input("Podaj wynagrodzenie: "))
lata_pracy = int(input("Podaj liczbę lat pracy: "))

if lata_pracy > 5:
    print("Bonus wynosi", 0.05*wynagrodzenie)
else:
    print("Brak bonusu")
