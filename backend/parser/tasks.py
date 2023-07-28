from backend.celery import app
from backend.redis import redis_connection
from backend.settings import PARSER_LINK
from parser.models import Product
from parser.utils import parse_pages


@app.task
def parsing_start(count: int):
    product_list = parse_pages(PARSER_LINK, count)

    Product.objects.all().delete()
    for product in product_list:
        Product.objects.create(name=product['name'], url=product['url'])

    redis_connection.lpush('parser', f'parser complete {len(product_list)}')
    return len(product_list)
