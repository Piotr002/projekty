import requests
from bs4 import BeautifulSoup
import json

def download_value_of_currency():
    """Funkcja pobierająca kursy walut z internetu."""
    index_url = "https://www.nbp.pl/home.aspx?f=/kursy/kursya.html"

    r = requests.get(index_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tabela = soup.find_all("table")
    for i in tabela:
        if "bat (Tajlandia)" in str(i):
            my_data = tabela[tabela.index(i)]
            prepare_for_table = [link.string for link in
                                 my_data.find_all('td')]  # zwraca nazwę, waluty, kod waluty i kurs
            name = []
            courses = []
            for j in range(1, len(prepare_for_table), 3):
                name.append(prepare_for_table[j])
            for j in range(2, len(prepare_for_table), 3):
                courses.append(prepare_for_table[j])
            for j in range(len(courses)):
                courses[j] = courses[j].replace(',', '.')
            for j in range(len(name)):
                if name[j].split()[0] != '1':
                    courses[j] = str(float(courses[j]) / int(name[j].split()[0]))
                name[j] = name[j][-3:]
            return name, courses


def table():
    """Funkcja tworząca tabelkę z kursami walut"""
    json_dict = {'PLN': '1.0000'}
    for i in range(len(download_value_of_currency()[0])):
        json_dict[download_value_of_currency()[0][i]] = download_value_of_currency()[1][i]
    with open("tabela.json", 'w') as j:
        json.dump(json_dict, j)

if __name__ == "__main__":
    table()