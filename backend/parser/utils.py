import time
from selenium import webdriver
from bs4 import BeautifulSoup


def convert_to_number(string_with_number: str) -> int:
    cleaned_string = ''.join(filter(str.isdigit, string_with_number))
    number = int(cleaned_string)
    return number


def parse_page(url: str) -> list:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.execute_script("window.scrollTo(5,4000);")
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # get all product cards
    cards = soup.find_all('div', {'data-widget': 'searchResultsV2'})[0]
    hrefs = cards.find_all('a')
    url_list = []
    name_list = []

    for href in hrefs:
        if 'https://www.ozon.ru' + href['href'] in url_list:
            name_list.append(href.find_all('span')[0].text)
        else:
            url_list.append('https://www.ozon.ru' + href['href'])

    products = list(zip(name_list, url_list))

    list_products = []
    for product in products:
        list_products.append({'name': product[0], 'url': product[1]})
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
