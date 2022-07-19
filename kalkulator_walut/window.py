from tkinter import Tk, StringVar
from tkinter.ttk import *
import tkinter.messagebox as msb
import json
from net_data import *


class window:
    """Przygotowuje okno, do przeliczania kursów walut."""

    def unpack_table(self):
        """Funkcja rozpakowująca tabelkę z formatu json.
        :return: listy nazw i kursów walut.
        :rtype: tuple
        """
        unpack = open("tabela.json", 'r')
        unpack = json.load(unpack)
        name = []
        courses = []
        for key, val in iter(unpack.items()):
            name.append(key)
            courses.append(val)
        return name, courses

    def count(self):
        """Funkcja obliczająca wartość waluty. Funkcja obsługuje ułamki, gdzie zamiast kropki, urzytkownik wsawi przecinek."""
        kwota = self.kwota.get()
        if kwota.count(",") == 1:
            kwota = kwota.replace(',', '.')
        if self.subtext1.get() == "Super!\n" and self.subtext2.get() == "Super!\n":
            if kwota == "":
                msb.showinfo("Info", "Wprowadź kwotę")
            else:
                try:
                    indeks_waluty = self.name.index(self.cb_value1.get())
                    indeks_waluty_docelowej = self.name.index(self.cb_value2.get())
                    self.text.set(
                        f'{round(float(kwota) * (float(self.courses[indeks_waluty_docelowej]) / float(self.courses[indeks_waluty])), 2)}')
                    self.subtext3.set("Super!\n")
                except:
                    self.subtext3.set("Ajajaj\n")
                    msb.showerror("Błąd", "Podana kwota ma być liczbą")
        else:
            msb.showinfo("Info", "Wybierz waluty")

    def quit(self):
        """Funkcja kończąca pracę okienka.
        """
        import sys
        sys.exit()

    def keycodess(self, event):
        """Funkcja obsługująca zdarzenia klawiszy. Enter - policz, Escape - zakończ."""
        if event.keysym == 'Return':
            self.count()
        if event.keysym == 'Escape':
            self.quit()

    def select1(self, event):
        """Funkcja ustawiająca tekst pod pierwszą listą rozwijaną oraz ewentualnie pod polem do wpisania kwoty."""
        self.subtext1.set("Super!\n")
        if self.subtext2.get() == "Super!\n":
            self.subtext3.set("Jeszcze tylko wprowadź\nkwotę i zatwierdź")

    def select2(self, event):
        """Funkcja ustawiająca tekst pod drugą listą rozwijaną oraz ewentualnie pod polem do wpisania kwoty."""
        self.subtext2.set("Super!\n")
        if self.subtext1.get() == "Super!\n":
            self.subtext3.set("Jeszcze tylko wprowadź\nkwotę i zatwierdź")

    def __init__(self, master):
        """Funkcja initująca okienko, ustawiawiająca lokalizację przycisków, list rozwijanych,
        napisów oraz pola do wpisywania kwoty. Funkcja obsługuje wyjątki (np. złe wpianie kwoty/niewpisanie kwoty/brak wyboru walut)."""

        # kwoty i waluty
        self.name = self.unpack_table()[0]
        self.courses = self.unpack_table()[1]

        # ramka z napisem 'waluta', listą rozwijaną z walutami i 'elastycznym napisem'
        self.left_frame = Frame(master)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)
        self.waluta = Label(self.left_frame, text="Waluta")
        self.waluta.pack()
        self.cb_value1 = StringVar()
        self.lista_walut = Combobox(self.left_frame, textvariable=self.cb_value1, state="readonly")
        self.lista_walut['values'] = self.name
        self.lista_walut.pack()
        self.subtext1 = StringVar()
        self.subtext1.set("Wybierz\nwalutę")
        self.subtext1_ = Label(self.left_frame, textvariable=self.subtext1)
        self.subtext1_.pack()
        self.lista_walut.bind("<<ComboboxSelected>>", self.select1)
        # ramka z napisem 'waluta docelowa', listą rozwijaną z walutami i 'elastycznym napisem'
        self.top_frame = Frame(master)
        self.top_frame.grid(row=0, column=1, padx=10, pady=10)
        self.waluta_docelowa = Label(self.top_frame, text="Waluta docelowa")
        self.waluta_docelowa.pack()
        self.cb_value2 = StringVar()
        self.lista_walut_docelowych = Combobox(self.top_frame, textvariable=self.cb_value2, state="readonly")
        self.lista_walut_docelowych['values'] = self.name
        self.lista_walut_docelowych.pack()
        self.subtext2 = StringVar()
        self.subtext2.set("Wybierz walutę\ndocelową")
        self.subtext2_ = Label(self.top_frame, textvariable=self.subtext2)
        self.subtext2_.pack()
        self.lista_walut_docelowych.bind("<<ComboboxSelected>>", self.select2)

        # ramka z napisem 'wpisz kwotę', polem do wpisania kwoty i 'elastycznym napisem'
        self.right_frame = Frame(master)
        self.right_frame.grid(row=0, column=2, padx=10, pady=10)
        self.kwota_txt = Label(self.right_frame, text="Podaj kwotę")
        self.kwota_txt.pack()
        self.kwota = Entry(self.right_frame, width=20)
        self.kwota.pack()
        self.subtext3 = StringVar()
        self.subtext3.set("\n")
        self.subtext3_ = Label(self.right_frame, textvariable=self.subtext3)
        self.subtext3_.pack()

        # ramka z przyciskiem uruchamiającym obliczenia
        self.frame = Frame(master)
        self.frame.grid(row=1, column=2, padx=10, pady=10)
        self.policz = Button(self.frame, text="Przelicz", command=self.count)
        self.policz.pack()

        # ramka z napisem 'wynik', miescem do wyświetlenia wyniku i przyciskiem do zakończenia pracy programu
        self.middle_frame = Frame(master)
        self.middle_frame.grid(row=2, column=1, padx=10, pady=10)
        self.wynik = Label(self.middle_frame, text='Wynik', font=15)
        self.wynik.pack()
        self.text = StringVar()
        self.text.set("")
        self.wynik_text = Label(self.middle_frame, textvariable=self.text, font=10)
        self.wynik_text.pack(pady=10)
        self.exit = Button(self.middle_frame, text='Zakończ', command=self.quit)
        self.exit.pack(pady=10)

        master.bind_all('<Key>', self.keycodess) # obsługa klawiszy
