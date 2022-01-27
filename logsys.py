import pyautogui
__author__= 'konsola'
print ('Prosty system logowania')
login = input('Podaj login:')
haslo = input('Podaj hasło: ')
if login== 'admin' and haslo== 'rem' :
    print ('Zalogowałeś się poprawnie')
    print ('Co chcesz zrobić? ')
    akcja = input('1 = ZMIENIĆ LOGIN, 2 = ZMIENIĆ HASŁO, 3 = WYLOGOWAĆ SIĘ')
    if akcja == "1":
        # = input('Podaj nowy login:')
    elif akcja =="2":
        zmianah = input ('Podaj nowe hasło:')
    elif akcja =="3":
        print("WYLOGOWANO...")
    else:
        print('Brak lub niewłaściwa akcja:')
else:
    print("BŁĄD!!!")