from django.urls import reverse, resolve
from accounts.views import vendor_dashboard
from vendor.views import vendor_order, vendor_profile, vendor_orders, add_product, product, products, delete_product, opening_hours, add_opening_hour, delete_opening_hour

class TestUrls:
    def test_vendor_dashboard(self):
        path = reverse('vendor')
        print('path is: ', path)
        assert resolve(path).func == vendor_dashboard

    def test_vendor_profile(self):
        path = reverse('vendor_profile')
        print('path is: ', path)
        assert resolve(path).func == vendor_profile

    def test_vendor_orders(self):
        path = reverse('vendor_orders')
        print('path is: ', path)
        assert resolve(path).func == vendor_orders
    
    def test_vendor_order(self):
        path = reverse('vendor_order', args=[1])
        print('path is: ', path)
        assert resolve(path).func == vendor_order


    def test_products(self):
        path = reverse('products')
        print('path is: ', path)
        assert resolve(path).func == products
    
    def test_product(self):
        path = reverse('product', args=[1])
        print('path is: ', path)
        assert resolve(path).func == product

    def test_add_product(self):
        path = reverse('add_product')
        print('path is: ', path)
        assert resolve(path).func == add_product

    def test_detele_product(self):
        path = reverse('delete_product', args=[1])
        print('path is: ', path)
        assert resolve(path).func == delete_product

    
    def test_add_opening_hour(self):
        path = reverse('add_opening_hour')
        print('path is: ', path)
        assert resolve(path).func == add_opening_hour

    def test_opening_hours(self):
        path = reverse('opening_hours')
        print('path is: ', path)
        assert resolve(path).func == opening_hours

    def test_detele_opening_hour(self):
        path = reverse('delete_opening_hour', args=[1])
        print('path is: ', path)
        assert resolve(path).func == delete_opening_hour



