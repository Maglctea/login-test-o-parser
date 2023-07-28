import time
from selenium import webdriver
from bs4 import BeautifulSoup

from backend.settings import PARSER_LINK

PRICE = 'c3-a1'
NAME = 'xd3 d4x'
CARD = 'ij8 j8i'


def convert_to_number(string_with_number: str) -> int:
    # Удаляем ненужные символы
    cleaned_string = ''.join(filter(str.isdigit, string_with_number))

    # Преобразуем строку в число
    number = int(cleaned_string)

    return number


def parse_page(url: str) -> list:
    list_products = []

    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    driver.execute_script("window.scrollTo(5,4000);")
    time.sleep(5)
    options.headless = True  # invisible browser window

    # creating BeautifulSoup object
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # get all product cards
    cards = soup.find_all('div', class_=CARD)
    for card in cards:
        image_url = card.find_all('img')[0]['src']
        name = card.find_all('div', class_=NAME)[0].text
        url = 'https://www.ozon.ru' + card.find_all('a')[0]['href']
        price = convert_to_number(card.find_all(class_=PRICE)[0].text)

        list_products.append({'name': name, 'price': price, 'url': url, 'image_url': image_url})
    return list_products


def parse_pages(url: str, count_products: int) -> list:
    list_products = []
    page = 1
    while len(list_products) < count_products:
        current_url = f'{url}?miniapp=seller_1&page={page}'
        current_list_page = parse_page(current_url)
        if current_list_page:
            list_products += current_list_page
            page += 1
        else:
            break
    return list_products[:count_products]


s = parse_pages(PARSER_LINK, 10)
pass