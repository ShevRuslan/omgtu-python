import requests
from bs4 import BeautifulSoup
def parse():
    url = 'https://omgtu.ru/general_information/faculties/' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.findAll('div', class_='project-description') # находим  контейнер с нужным классом
    faculties = []
    for faculty in soup.select('div#pagecontent > ul > li > a > span'):
        faculties.append(faculty.text.strip())
    for faculty in soup.select('div#pagecontent > ul > li > span > a'):
        faculties.append(faculty.text.strip())
    with open('faculties.txt', 'w', encoding='utf-8') as f:
        for faculty in faculties:
            f.write(faculty + '\n')
parse()