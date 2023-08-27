from django.test import TestCase
from restaurant.models import Menu

class test_menu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=2, inventory=100)
        self.assertEqual(item, "IceCream : 2")