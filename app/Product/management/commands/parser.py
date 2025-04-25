import requests
from bs4 import BeautifulSoup



def get_category(url):

    categories = []
    category_name = []

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    categories_link = soup.find('div', class_='common__categories').ul
    category = categories_link.find_all('li')
    for i in category:
        el = url + i.find('a').get('href')
        category_name.append(i.find('a').text.strip())
        categories.append(el)

    return categories, category_name


def get_product(url):

    products = []

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    carts = soup.find_all('div', class_='common__recommendations__list__item one-four')

    for cart in carts:

        if cart.find('div', class_='common__recommendations__list__item__price__current no-old'):
            price = cart.find('div', class_='common__recommendations__list__item__price__current no-old').text
        else:
            price = cart.find('div', class_='common__recommendations__list__item__price__current').text

        name = cart.find('div', class_='common__recommendations__list__item__title').find('a').text
        link = url + cart.find('div', class_='common__recommendations__list__item__img').find('a').get('href')
        img_link = cart.find('div', class_='common__recommendations__list__item__img').find('a').get('data-background-image')

        product = {'name' : name,
                   'link' : link,
                   'img_link' : img_link,
                   'price' : price
                   }
        
        products.append(product)

    return products