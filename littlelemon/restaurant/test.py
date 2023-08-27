from django.test import TestCase
from restaurant.models import Menu

class test_menu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=3,title="IceCream", price=2, inventory=100)
        itemstr = item.__str__()
        self.assertEqual(itemstr, "IceCream : 2")

