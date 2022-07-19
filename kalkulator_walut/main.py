from window import *

if __name__ == "__main__":
    """Uruchomienie programu - w zależności od dostępu do internetu."""
    try:
        download_value_of_currency()
        table()
        root = Tk()
        root.geometry('480x280+640+360')
        root.title('Przeliczanie walut')
    except:
        root = Tk()
        root.geometry('480x280+640+360')
        root.title('Przeliczanie walut')
    my_window = window(root)
    root.mainloop()