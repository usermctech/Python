# odliczanie od 1 do określonej wartości
licznik = 1
while licznik < 10:
    print(f"Wartość licznika to {licznik}")
    licznik += 1
    print(f"Wartość po dodaniu 1 to {licznik}")
    print("-----")

# odliczanie, dopóki wartość jest większa niż zero
licznik = 10
while licznik:
    print(f"Wartość licznika to {licznik}")
    licznik -= 1
    print(f"Wartość po zmiejszeniu 1 to {licznik}")
    print("-----")

# pętla z wykorzystaniem sprawdzenia wartości zmiennej
x = 1
stop = False
while not stop:
    x += 3
    print(f"Wartość x = {x}")
    if x > 25:
        print("Kończymy...")
        stop = True
    if x > 20:
        print("Przekroczyliśmy 20...")
