from django.core.management.base import BaseCommand
from restaurant.models import MenuItem

class Command(BaseCommand):
    help = 'Populate the menu with initial data'

    def handle(self, *args, **kwargs):
        menu_items = [
            {
                'title': 'Greek Salad',
                'price': 12.99,
                'inventory': 100,
                'category': 'appetizer',
                'description': 'Fresh Mediterranean salad with olives and feta cheese'
            },
            {
                'title': 'Bruschetta',
                'price': 8.99,
                'inventory': 100,
                'category': 'appetizer',
                'description': 'Grilled bread with tomatoes, garlic, and fresh basil'
            },
            {
                'title': 'Grilled Fish',
                'price': 25.99,
                'inventory': 50,
                'category': 'main',
                'description': 'Fresh catch of the day with seasonal vegetables'
            },
            {
                'title': 'Pasta Carbonara',
                'price': 18.99,
                'inventory': 70,
                'category': 'main',
                'description': 'Classic Italian pasta with eggs, cheese, and pancetta'
            },
            {
                'title': 'Tiramisu',
                'price': 9.99,
                'inventory': 40,
                'category': 'dessert',
                'description': 'Classic Italian coffee-flavored dessert'
            },
            {
                'title': 'House Wine',
                'price': 7.99,
                'inventory': 100,
                'category': 'drink',
                'description': 'Glass of our house red or white wine'
            },
        ]

        for item in menu_items:
            MenuItem.objects.get_or_create(
                title=item['title'],
                defaults={
                    'price': item['price'],
                    'inventory': item['inventory'],
                    'category': item['category'],
                    'description': item['description']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated menu items'))
