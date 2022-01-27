wrozba = 0
imie = input("Jak się nazywasz?")
print("Witaj, "+imie+"!")
wrozba = int(input("Podaj numer z zakresu 1-10"))
if wrozba == 1:
    print("Znajdziesz coś interesującego")
elif wrozba == 2:
    print("Patrz pod nogi! Znajdziesz coś wartościowego.")
elif wrozba == 3:
    print("Patrz w niebo!")
elif wrozba == 4:
    print("Spełni się jedno z Twoich marzeń!")
elif wrozba == 5:
    print("Znajdziesz coś czego bardzo długo szukałeś.")
elif wrozba == 6:
    print("Ktoś wykupi pożądany przez Ciebie produkt.")
elif wrozba == 7:
    print("W ciągu godziny spotka cię pech...")
elif wrozba == 8:
    print("Znajdziesz przyjaciela/przyjaciółkę")
elif wrozba == 9:
    print("Kupisz coś zbędnego.")
elif wrozba == 10:
    print("Dzisiaj będzie twój sczęśliwy dzień!")
else:
    print("Podaj poprawny numer lub wyjdź..")
    wrozba = int(input("Podaj numer z zakresu 1-10"))