import json

from django.test import TestCase
from django.urls import reverse

from .models import Command, Flavour, Stock

class ViewsTest(TestCase):

    # new
    def test_should_list_all_available_flavours(self):
        count_flavour = Flavour.objects.count()
        url = reverse("ice_cream:new")
        response = self.client.post(url, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('stocks' in response.context)
        self.assertEqual(count_flavour, len(response.context['stocks']))

    # create
    def test_should_create_command(self):
        data = 'Cherry=5'
        url = reverse("ice_cream:create")

        cherry = Flavour.objects.get(name='Cherry')
        self.assertEqual(Stock.objects.get(flavour=cherry).amount, 40)
        response = self.client.post(url, data, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Stock.objects.get(flavour=cherry).amount, 35)

        self.assertFalse("error_message" in response.context)
        self.assertTrue("command" in response.context)
        command = response.context['command']
        self.assertTrue(type(command) == Command)
        self.assertTrue(command.price)
        self.assertTrue(command.code)

    def test_should_warn_for_empty_command(self):
        url = reverse("ice_cream:create")
        response = self.client.post(url, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertFalse("command" in response.context)
        self.assertTrue("error_message" in response.context)

    def test_should_warn_for_command_when_low_stock(self):
        data = 'Cherry=5'
        url = reverse("ice_cream:create")

        cherry = Flavour.objects.get(name='Cherry')
        stock = Stock.objects.get(flavour=cherry)
        stock.amount=2
        stock.save()
        self.assertEqual(2, stock.amount)

        response = self.client.post(url, data, content_type='application/x-www-form-urlencoded')
        
        self.assertEqual(response.status_code, 200)
        self.assertFalse("command" in response.context)
        self.assertTrue("error_message" in response.context)

    # detail
    def test_should_get_detail_of_command_with_list_of_scoops(self):
        command = Command.objects.create(
            content=json.dumps({"Cherry": 5}),
            price=10)

        data = 'command_code=%s' % command.code
        url = reverse('ice_cream:detail')

        response = self.client.post(url, data, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertFalse("error_message" in response.context)
        self.assertTrue("command" in response.context)
        self.assertTrue("scoops" in response.context)
        self.assertEqual(5, len(response.context['scoops']))



    def test_should_warn_for_non_existing_command(self):
        data = 'command_code=12345678'
        url = reverse('ice_cream:detail')

        response = self.client.post(url, data, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertFalse("command" in response.context)
        self.assertFalse("scoops" in response.context)
        self.assertTrue("error_message" in response.context)

    # admin
    def test_should_get_detail_of_admin(self):
        count_flavour = Flavour.objects.count()

        url = reverse('ice_cream:admin')

        response = self.client.post(url, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        self.assertTrue("revenue" in response.context)
        self.assertTrue("stocks" in response.context)
        self.assertEqual(count_flavour, len(response.context['stocks']))
        

    def test_should_refill_stock_in_admin(self):
        cherry = Flavour.objects.get(name='Cherry')
        stock = Stock.objects.get(flavour=cherry)
        stock.amount=2
        stock.save()
        self.assertEqual(2, stock.amount)

        data = 'Cherry'

        url = reverse('ice_cream:admin')
        response = self.client.post(url, data, content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 200)
        stock = Stock.objects.get(flavour=cherry)
        self.assertEqual(40, stock.amount)
        





