import sys, math, tkinter
from tkinter import *
from tkinter import messagebox
 
def wyjscie():
    pytanie = messagebox.askyesno(title = "Wyjście z programu", message = "Czy chcesz zakończyć pracę?")
    if pytanie:
        sys.exit()
 
def o_programie():
    messagebox.showinfo(title = "Kalkulator v. 0.1", message = "by"  "Maksymilian Lepich")
 
def memory_null():
    zmienna.memory = "0"
    labelka_memory.configure(text = str(zmienna.memory))
 
def memory_add():
    zmienna.memory = zmienna.summary
    zmienna.summary = "0"
    labelka_memory.configure(text = str(zmienna.memory))
    summary_update()
 
def memory_use():
    if zmienna.memory != "0":
        zmienna.summary = zmienna.memory
        zmienna.memory = "0"
        labelka_memory.configure(text = str(zmienna.memory))
        summary_update()
 
def zerowanie():
    zmienna.memory = "0"
    zmienna.history = ""
    zmienna.summary = "0"
    zmienna.dzialanie = 6
    summary_update()
 
def obliczenie(numer):
    if zmienna.history == "":
        if zmienna.summary != "0":
            zmienna.history = zmienna.summary
            zmienna.summary = "0"
            zmienna.dzialanie = numer
    else:
        zmienna.dzialanie = numer
        zapis()
        if zmienna.dzialanie == 0:
            zmienna.summary = float(zmienna.history) + float(zmienna.summary)
        elif zmienna.dzialanie == 1:
            zmienna.summary = float(zmienna.history) - float(zmienna.summary)
        elif zmienna.dzialanie == 2:
            zmienna.summary = float(zmienna.history) * float(zmienna.summary)
        elif zmienna.dzialanie == 3:
            if float(zmienna.summary) != 0:
                zmienna.summary = float(zmienna.history) / float(zmienna.summary)
        elif zmienna.dzialanie == 4:
            zmienna.summary = float(zmienna.history) ** float(zmienna.summary)
        elif zmienna.dzialanie == 5:
            zmienna.summary = math.sqrt(float(zmienna.summary))
        if zmienna.dzialanie != 6:
            zmienna.history = zmienna.summary
            zmienna.summary = "0"
    summary_update()
 
def zapis():
    plik = open("histkalk.txt","a")
    plik.write(str(zmienna.history) + " " + str(zmienna.l_f[zmienna.dzialanie]) + " " + str(zmienna.summary) + "\n")
    plik.close()
 
def rownanie():
    obliczenie(zmienna.dzialanie)
 
def przecinek():
    if zmienna.summary.count(".") > 0:
        zmienna.summary = zmienna.summary.replace(".","")
        zmienna.summary += "."
    else:
        zmienna.summary += "."
    summary_update()
 
def cyfrowanie(numer):
    if zmienna.summary == "0":
        zmienna.summary = str(numer)
    else:
        zmienna.summary += str(numer)
    summary_update()
 
def summary_update():
    if zmienna.dzialanie >= 6:
        labelka_summary.configure(text = str(zmienna.history) + "\n" + str(zmienna.summary))
    else:
        labelka_summary.configure(text = str(zmienna.history) + " " + str(zmienna.l_f[zmienna.dzialanie]) + "\n" + str(zmienna.summary))
 
class zmienna():
    memory = "0"
    summary = "0"
    history = ""
    dzialanie = 6
    p_f = []
    p_m = []
    p_n = []
    l_f = ["+","-","×","÷","^","√","="]
 
okno = tkinter.Tk()
okno.title("Kalkulator")
okno.resizable(False, False)
 
ramka_wyniki = Frame(okno, bg='black')
ramka_wyniki.grid(columnspan = 3, padx = (10, 10), pady = 10, sticky = E+W)
 
ramka_cyfry = Frame(okno)
ramka_cyfry.grid(row = 1, column = 0, padx = (10, 10))
 
ramka_funkcje = Frame(okno)
ramka_funkcje.grid(row = 1, column = 1, padx = (10, 10))
 
ramka_pamiec = Frame(okno)
ramka_pamiec.grid(row = 2, columnspan = 2, padx = (10, 10), pady = 10)
 
labelka_summary = Label(ramka_wyniki, text = str(zmienna.summary), bg = "#000000", fg = "#00FF00", justify = RIGHT)
labelka_memory = Label(ramka_pamiec, text = str(zmienna.memory))
labelka_summary.pack(fill = BOTH, side = RIGHT, expand = False)
labelka_memory.grid(row = 1, columnspan = 3)
 
for przycisk in zmienna.l_f:
    dlugosc = len(zmienna.p_f)
    if dlugosc != 6:
        zmienna.p_f.append(Button(ramka_funkcje, text = przycisk, command = lambda b = dlugosc: obliczenie(b)))
    else:
        zmienna.p_f.append(Button(ramka_funkcje, text = przycisk, command = lambda: rownanie()))
    zmienna.p_f[dlugosc].grid(row = math.floor(dlugosc / 2), column = dlugosc % 2, sticky = W+E)
zmienna.p_f.append(Button(ramka_funkcje, text = "C", bg = "#FF0000", fg = "#FFFFFF", command = zerowanie))
zmienna.p_f[7].grid(row = 3, column = 1, sticky = W+E)
 
zmienna.p_m.append(Button(ramka_pamiec, text = "M+", command=memory_add))
zmienna.p_m.append(Button(ramka_pamiec, text = "Mem", command=memory_use))
zmienna.p_m.append(Button(ramka_pamiec, text = "MC", bg = "#FFC0CB", command = memory_null))
zmienna.p_m[0].grid(row=0, column=0)
zmienna.p_m[1].grid(row=0, column=1)
zmienna.p_m[2].grid(row=0, column=2)
 
zmienna.p_n.append(Button(ramka_cyfry, text="0", command=lambda:cyfrowanie(0)))
zmienna.p_n[0].grid(row=3, column=0, columnspan=2, sticky=W+E)
for cyfra in range(1,10):
    dlugosc=len(zmienna.p_n)
    zmienna.p_n.append(Button(ramka_cyfry, text=cyfra, command=lambda b=dlugosc:cyfrowanie(b)))
    zmienna.p_n[dlugosc].grid(row=2-math.floor((dlugosc-1)/3), column=(dlugosc-1) % 3, sticky=W+E)
zmienna.p_n.append(Button(ramka_cyfry, text=",", command=przecinek))
zmienna.p_n[10].grid(row=3, column=2, sticky=W+E)
 
topmenu = Menu(okno)
topmenu.add_command(label="O programie", command=o_programie)
topmenu.add_command(label="Wyjście", command=wyjscie)
 
okno.config(menu=topmenu)
zerowanie()
okno.mainloop()
