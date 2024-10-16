from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name="Фрукты", description="Очень сладкие")

        products = [
            {'name': "Клубника", 'category': category, 'price': 350, 'created_at': "2024-01-01"},
            {'name': "Малина", 'category': category, 'price': 400, 'created_at': "2024-02-02"},
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Товар: {product.name} добавлен успешно!'))
            else:
                self.stdout.write(self.style.WARNING(f'Товар: {product.name} уже имеется в каталоге!'))
