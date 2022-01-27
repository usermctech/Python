print("hasło to: MATEMATYKA")
hasło = "xxx"
while hasło != "MATEMATYKA":
    hasło = input("Podaj hasło :")
    if hasło != "admin":
        print ("ZŁE HASŁO ! ")
print("Hasło poprawne...")
print("Możesz uzyskać dostęp do zasobu...")
obliczenia = "tak"
while obliczenia == "tak":
     print ("Witaj w kalkulatorze!")
     a = int(input("Podaj pierwszą liczbę:"))
     b = int(input("Podaj drugą liczbę:"))
     print ("dodawanie:")
     print (a + b)
     print ("odejmowanie:")
     print (a - b)
     print ("mnożenie:")
     print (a * b)
     print ("dzielenie:")
     if b == 0:
         print ("BŁĄD!!! ,Nie wolno dzielić przez 0!")
     else:
         print(a / b)
     obliczenia = input("Czy chcesz wykonać inne obliczenie? (tak/nie) ")
