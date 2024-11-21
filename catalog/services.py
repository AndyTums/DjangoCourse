from .models import Product
from django.core.cache import cache
from config.settings import CACHE_ENABLE


def get_products_from_cache():
    """ Низкоуровневое кэширование продуктов """

    if not CACHE_ENABLE:
        return Product.objects.all()
    key = "products_list"
    info_cache = cache.get(key)
    if info_cache is not None:
        return info_cache
    info_cache = Product.objects.all()
    cache.set(key, info_cache)
    return info_cache


class ProductService:

    @staticmethod
    def get_products_category(category_id):
        products = Product.objects.filter(category=category_id)

        return products
